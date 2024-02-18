# torchcell/adapters/kuzmin2018_adapter.py
# [[torchcell.adapters.kuzmin2018_adapter]]
# https://github.com/Mjvolk3/torchcell/tree/main/torchcell/adapters/kuzmin2018_adapter.py
# Test file: tests/torchcell/adapters/test_kuzmin2018_adapter.py

from tqdm import tqdm
import hashlib
import random
import string
from enum import Enum, auto
from functools import lru_cache
from itertools import chain
from typing import Optional
import json
import pandas as pd
from biocypher._create import BioCypherEdge, BioCypherNode
from biocypher._logger import logger
from typing import Generator, Set
from torchcell.datasets.scerevisiae import (
    SmfKuzmin2018Dataset,
    DmfKuzmin2018Dataset,
    TmfKuzmin2018Dataset,
)
from torchcell.datamodels.schema import (
    Genotype,
    SgaAllelePerturbation,
)
from sortedcontainers import SortedList
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
import torch

logger.debug(f"Loading module {__name__}.")


class SmfKuzmin2018Adapter:
    def __init__(self, dataset: SmfKuzmin2018Dataset, num_workers: int):
        self.dataset = dataset
        self.num_workers = num_workers

    def get_nodes(self):
        methods = [
            self._get_experiment_reference_nodes,
            self._get_genome_nodes,
            self._get_experiment_nodes,
            self._get_dataset_nodes,
            self._get_genotype_nodes,
            self._get_environment_nodes,
            self._get_media_nodes,
            self._get_temperature_nodes,
            self._get_phenotype_nodes,
        ]

        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(method) for method in methods]

            for future in as_completed(futures):
                try:
                    node_generator = future.result()
                    for node in node_generator:
                        yield node
                except Exception as exc:
                    logger.error(
                        f"Node generation method generated an exception: {exc}"
                    )

    def _get_experiment_reference_nodes(self) -> None:
        nodes = []
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            node = BioCypherNode(
                node_id=experiment_ref_id,
                preferred_id=f"SmfKuzmin2018_reference_{i}",
                node_label="experiment reference",
                properties={
                    "dataset_index": i,
                    "serialized_data": json.dumps(data.reference.model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_genome_nodes(self) -> None:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            genome_id = hashlib.md5(
                json.dumps(data.reference.reference_genome.model_dump()).encode("utf-8")
            ).hexdigest()

            if genome_id not in seen_node_ids:
                seen_node_ids.add(genome_id)
                node = BioCypherNode(
                    node_id=genome_id,
                    preferred_id=f"reference_genome_{i}",
                    node_label="genome",
                    properties={
                        "species": data.reference.reference_genome.species,
                        "strain": data.reference.reference_genome.strain,
                        "serialized_data": json.dumps(
                            data.reference.reference_genome.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_experiment_nodes(self) -> None:
        nodes = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()

            node = BioCypherNode(
                node_id=experiment_id,
                preferred_id=f"SmfKuzmin2018_{i}",
                node_label="experiment",
                properties={
                    "dataset_index": i,
                    "serialized_data": json.dumps(data["experiment"].model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_genotype_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            genotype_id = hashlib.md5(
                json.dumps(data["experiment"].genotype.model_dump()).encode("utf-8")
            ).hexdigest()

            if genotype_id not in seen_node_ids:
                seen_node_ids.add(genotype_id)
                systematic_gene_name = data[
                    "experiment"
                ].genotype.perturbation.systematic_gene_name
                perturbed_gene_name = data[
                    "experiment"
                ].genotype.perturbation.perturbed_gene_name
                description = data["experiment"].genotype.perturbation.description
                perturbation_type = data[
                    "experiment"
                ].genotype.perturbation.perturbation_type

                self._get_perturbation(data["experiment"].genotype)

                node = BioCypherNode(
                    node_id=genotype_id,
                    preferred_id=f"genotype_{i}",
                    node_label="genotype",
                    properties={
                        "systematic_gene_names": [systematic_gene_name],
                        "perturbed_gene_names": [perturbed_gene_name],
                        "is_deletion_genotype": isinstance(
                            data["experiment"].genotype, Genotype
                        ),
                        "is_interference_genotype": isinstance(
                            data["experiment"].genotype, Genotype
                        ),
                        "description": description,
                        "perturbation_types": [perturbation_type],
                        "serialized_data": json.dumps(
                            data["experiment"].genotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    @staticmethod
    def _get_perturbation(
        genotype: Genotype,
    ) -> Generator[BioCypherNode, None, None]:
        nodes = []
        if genotype.perturbation:
            i = 1
            perturbation_id = hashlib.md5(
                json.dumps(genotype.perturbation.model_dump()).encode("utf-8")
            ).hexdigest()

            node = BioCypherNode(
                node_id=perturbation_id,
                preferred_id=f"perturbation_{i}",
                node_label="perturbation",
                properties={
                    "systematic_gene_name": [
                        genotype.perturbation.systematic_gene_name
                    ],
                    "perturbed_gene_name": [genotype.perturbation.perturbed_gene_name],
                    "description": genotype.perturbation.description,
                    "perturbation_type": genotype.perturbation.perturbation_type,
                    "strain_id": genotype.perturbation.strain_id,
                    "serialized_data": json.dumps(genotype.perturbation.model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_environment_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()

            node_id = environment_id

            if node_id not in seen_node_ids:
                seen_node_ids.add(node_id)
                media = json.dumps(data["experiment"].environment.media.model_dump())

                node = BioCypherNode(
                    node_id=node_id,
                    preferred_id=f"environment_{i}",
                    node_label="environment",
                    properties={
                        "temperature": data["experiment"].environment.temperature.value,
                        "media": media,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["reference"].reference_environment.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            node_id = environment_id

            if node_id not in seen_node_ids:
                seen_node_ids.add(node_id)
                media = json.dumps(
                    data["reference"].reference_environment.media.model_dump()
                )

                node = BioCypherNode(
                    node_id=node_id,
                    preferred_id=f"environment_{i}",
                    node_label="environment",
                    properties={
                        "temperature": data[
                            "reference"
                        ].reference_environment.temperature.value,
                        "media": media,
                        "serialized_data": json.dumps(
                            data["reference"].reference_environment.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_media_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            media_id = hashlib.md5(
                json.dumps(data["experiment"].environment.media.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            if media_id not in seen_node_ids:
                seen_node_ids.add(media_id)
                name = data["experiment"].environment.media.name
                state = data["experiment"].environment.media.state

                node = BioCypherNode(
                    node_id=media_id,
                    preferred_id=f"media_{media_id}",
                    node_label="media",
                    properties={
                        "name": name,
                        "state": state,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.media.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        for i, data in tqdm(enumerate(self.dataset)):
            media_id = hashlib.md5(
                json.dumps(
                    data["reference"].reference_environment.media.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if media_id not in seen_node_ids:
                seen_node_ids.add(media_id)
                name = data["reference"].reference_environment.media.name
                state = data["reference"].reference_environment.media.state

                node = BioCypherNode(
                    node_id=media_id,
                    preferred_id=f"media_{media_id}",
                    node_label="media",
                    properties={
                        "name": name,
                        "state": state,
                        "serialized_data": json.dumps(
                            data["reference"].reference_environment.media.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_temperature_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            temperature_id = hashlib.md5(
                json.dumps(
                    data["experiment"].environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if temperature_id not in seen_node_ids:
                seen_node_ids.add(temperature_id)

                node = BioCypherNode(
                    node_id=temperature_id,
                    preferred_id=f"temperature_{temperature_id}",
                    node_label="temperature",
                    properties={
                        "value": data["experiment"].environment.temperature.value,
                        "unit": data["experiment"].environment.temperature.unit,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.temperature.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        for i, data in tqdm(enumerate(self.dataset)):
            temperature_id = hashlib.md5(
                json.dumps(
                    data["reference"].reference_environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if temperature_id not in seen_node_ids:
                seen_node_ids.add(temperature_id)

                node = BioCypherNode(
                    node_id=temperature_id,
                    preferred_id=f"temperature_{temperature_id}",
                    node_label="temperature",
                    properties={
                        "value": data[
                            "reference"
                        ].reference_environment.temperature.value,
                        "description": data[
                            "reference"
                        ].reference_environment.temperature.description,
                        "serialized_data": json.dumps(
                            data[
                                "reference"
                            ].reference_environment.temperature.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_phenotype_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            phenotype_id = hashlib.md5(
                json.dumps(data["experiment"].phenotype.model_dump()).encode("utf-8")
            ).hexdigest()

            if phenotype_id not in seen_node_ids:
                seen_node_ids.add(phenotype_id)
                graph_level = data["experiment"].phenotype.graph_level
                label = data["experiment"].phenotype.label
                label_error = data["experiment"].phenotype.label_error
                fitness = data["experiment"].phenotype.fitness
                fitness_std = data["experiment"].phenotype.fitness_std

                node = BioCypherNode(
                    node_id=phenotype_id,
                    preferred_id=f"phenotype_{phenotype_id}",
                    node_label="phenotype",
                    properties={
                        "graph_level": graph_level,
                        "label": label,
                        "label_error": label_error,
                        "fitness": fitness,
                        "fitness_std": fitness_std,
                        "serialized_data": json.dumps(
                            data["experiment"].phenotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        # References
        for i, data in tqdm(enumerate(self.dataset)):
            # Get the phenotype ID associated with the experiment reference
            phenotype_id = hashlib.md5(
                json.dumps(data["reference"].reference_phenotype.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            if phenotype_id not in seen_node_ids:
                seen_node_ids.add(phenotype_id)
                graph_level = data["reference"].reference_phenotype.graph_level
                label = data["reference"].reference_phenotype.label
                label_error = data["reference"].reference_phenotype.label_error
                fitness = data["reference"].reference_phenotype.fitness
                fitness_std = data["reference"].reference_phenotype.fitness_std

                node = BioCypherNode(
                    node_id=phenotype_id,
                    preferred_id=f"phenotype_{phenotype_id}",
                    node_label="phenotype",
                    properties={
                        "graph_level": graph_level,
                        "label": label,
                        "label_error": label_error,
                        "fitness": fitness,
                        "fitness_std": fitness_std,
                        "serialized_data": json.dumps(
                            data["reference"].reference_phenotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_dataset_nodes(self) -> None:
        nodes = [
            BioCypherNode(
                node_id="SmfKuzmin2018",
                preferred_id="SmfKuzmin2018",
                node_label="dataset",
            )
        ]
        return nodes

    def get_edges(self):
        methods = [
            self._get_dataset_experiment_ref_edges,
            self._get_experiment_dataset_edges,
            self._get_experiment_ref_experiment_edges,
            self._get_genotype_experiment_edges,
            self._get_environment_experiment_edges,
            self._get_environment_experiment_ref_edges,
            self._get_phenotype_experiment_edges,
            self._get_phenotype_experiment_ref_edges,
            self._get_media_environment_edges,
            self._get_temperature_environment_edges,
            self._get_genome_edges,
        ]

        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(method) for method in methods]
            for future in as_completed(futures):
                try:
                    edge_generator = future.result()
                    for edge in edge_generator:
                        yield edge
                except Exception as exc:
                    logger.error(
                        f"Edge generation method generated an exception: {exc}"
                    )

    def _get_dataset_experiment_ref_edges(self):
        edges = []
        for data in self.dataset.experiment_reference_index:
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            edge = BioCypherEdge(
                source_id=experiment_ref_id,
                target_id="SmfKuzmin2018",
                relationship_label="experiment reference member of",
            )
            edges.append(edge)
        return edges

    def _get_experiment_dataset_edges(self):
        edges = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            edge = BioCypherEdge(
                source_id=experiment_id,
                target_id="SmfKuzmin2018",
                relationship_label="experiment member of",
            )
            edges.append(edge)
        return edges

    def _get_experiment_ref_experiment_edges(self):
        edges = []
        for data in tqdm(self.dataset.experiment_reference_index):
            dataset_subset = self.dataset[torch.tensor(data.index)]
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            for i, data in enumerate(dataset_subset):
                experiment_id = hashlib.md5(
                    json.dumps(data["experiment"].model_dump()).encode("utf-8")
                ).hexdigest()
                edge = BioCypherEdge(
                    source_id=experiment_ref_id,
                    target_id=experiment_id,
                    relationship_label="experiment reference of",
                )
                edges.append(edge)
        return edges

    def _get_genotype_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        # CHECK if needed - don't think needed since exp ref index
        # seen_genotype_experiment_pairs: Set[tuple] = set()
        edges = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            genotype_id = hashlib.md5(
                json.dumps(data["experiment"].genotype.model_dump()).encode("utf-8")
            ).hexdigest()

            self._get_perturbation_genotype_edges(
                genotype=data["experiment"].genotype, genotype_id=genotype_id
            )

            # CHECK if needed - don't think needed since exp ref index
            # genotype_experiment_pair = (genotype_id, experiment_id)
            # if genotype_experiment_pair not in seen_genotype_experiment_pairs:
            #     seen_genotype_experiment_pairs.add(genotype_experiment_pair)

            edge = BioCypherEdge(
                source_id=genotype_id,
                target_id=experiment_id,
                relationship_label="genotype member of",
            )
            edges.append(edge)
        return edges

    @staticmethod
    def _get_perturbation_genotype_edges(
        genotype: Genotype, genotype_id: str
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        if genotype.perturbation:
            perturbation_id = hashlib.md5(
                json.dumps(genotype.perturbation.model_dump()).encode("utf-8")
            ).hexdigest()

            edge = BioCypherEdge(
                source_id=perturbation_id,
                target_id=genotype_id,
                relationship_label="perturbation member of",
            )
            edges.append(edge)
        return edges

    def _get_environment_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_environment_experiment_pairs: Set[tuple] = set()
        # Linking environments to experiments
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()

            env_experiment_pair = (environment_id, experiment_id)
            if env_experiment_pair not in seen_environment_experiment_pairs:
                seen_environment_experiment_pairs.add(env_experiment_pair)

                edge = BioCypherEdge(
                    source_id=environment_id,
                    target_id=experiment_id,
                    relationship_label="environment member of",
                )
                edges.append(edge)
        return edges

    def _get_environment_experiment_ref_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_environment_experiment_ref_pairs: Set[tuple] = set()
        # Linking environments to experiment references
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            environment_id = hashlib.md5(
                json.dumps(data.reference.reference_environment.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            env_experiment_ref_pair = (environment_id, experiment_ref_id)
            if env_experiment_ref_pair not in seen_environment_experiment_ref_pairs:
                seen_environment_experiment_ref_pairs.add(env_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=environment_id,
                    target_id=experiment_ref_id,
                    relationship_label="environment member of",
                )
                edges.append(edge)
        return edges

    def _get_phenotype_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_phenotype_experiment_pairs: Set[tuple] = set()
        # Linking phenotypes to experiments
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            phenotype_id = hashlib.md5(
                json.dumps(data["experiment"].phenotype.model_dump()).encode("utf-8")
            ).hexdigest()

            phenotype_experiment_pair = (phenotype_id, experiment_id)
            if phenotype_experiment_pair not in seen_phenotype_experiment_pairs:
                seen_phenotype_experiment_pairs.add(phenotype_experiment_pair)

                edge = BioCypherEdge(
                    source_id=phenotype_id,
                    target_id=experiment_id,
                    relationship_label="phenotype member of",
                )
                edges.append(edge)

        return edges

    def _get_phenotype_experiment_ref_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_phenotype_experiment_ref_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            phenotype_id = hashlib.md5(
                json.dumps(data.reference.reference_phenotype.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            phenotype_experiment_ref_pair = (phenotype_id, experiment_ref_id)
            if phenotype_experiment_ref_pair not in seen_phenotype_experiment_ref_pairs:
                seen_phenotype_experiment_ref_pairs.add(phenotype_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=phenotype_id,
                    target_id=experiment_ref_id,
                    relationship_label="phenotype member of",
                )
                edges.append(edge)
        return edges

    def _get_media_environment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_media_environment_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()
            media_id = hashlib.md5(
                json.dumps(data["experiment"].environment.media.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            media_environment_pair = (media_id, environment_id)
            if media_environment_pair not in seen_media_environment_pairs:
                seen_media_environment_pairs.add(media_environment_pair)

                edge = BioCypherEdge(
                    source_id=media_id,
                    target_id=environment_id,
                    relationship_label="media member of",
                )
                edges.append(edge)
            return edges

    def _get_temperature_environment_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_temperature_environment_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()
            temperature_id = hashlib.md5(
                json.dumps(
                    data["experiment"].environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            temperature_environment_pair = (temperature_id, environment_id)
            if temperature_environment_pair not in seen_temperature_environment_pairs:
                seen_temperature_environment_pairs.add(temperature_environment_pair)

                edge = BioCypherEdge(
                    source_id=temperature_id,
                    target_id=environment_id,
                    relationship_label="temperature member of",
                )
                edges.append(edge)
        return edges

    def _get_genome_edges(self) -> None:
        edges = []
        seen_genome_experiment_ref_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            genome_id = hashlib.md5(
                json.dumps(data.reference.reference_genome.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            genome_experiment_ref_pair = (genome_id, experiment_ref_id)
            if genome_experiment_ref_pair not in seen_genome_experiment_ref_pairs:
                seen_genome_experiment_ref_pairs.add(genome_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=genome_id,
                    target_id=experiment_ref_id,
                    relationship_label="genome member of",
                )
                edges.append(edge)
        return edges


class DmfKuzmin2018Adapter:
    def __init__(self, dataset: DmfKuzmin2018Dataset, num_workers: int):
        self.dataset = dataset
        self.num_workers = num_workers

    def get_nodes(self):
        methods = [
            self._get_experiment_reference_nodes,
            self._get_genome_nodes,
            self._get_experiment_nodes,
            self._get_dataset_nodes,
            self._get_genotype_nodes,
            self._get_environment_nodes,
            self._get_media_nodes,
            self._get_temperature_nodes,
            self._get_phenotype_nodes,
        ]

        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(method) for method in methods]

            for future in as_completed(futures):
                try:
                    node_generator = future.result()
                    for node in node_generator:
                        yield node
                except Exception as exc:
                    logger.error(
                        f"Node generation method generated an exception: {exc}"
                    )

    def _get_experiment_reference_nodes(self) -> None:
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            nodes = []
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            node = BioCypherNode(
                node_id=experiment_ref_id,
                preferred_id=f"DmfKuzmin2018_reference_{i}",
                node_label="experiment reference",
                properties={
                    "dataset_index": i,
                    "serialized_data": json.dumps(data.reference.model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_genome_nodes(self) -> None:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            genome_id = hashlib.md5(
                json.dumps(data.reference.reference_genome.model_dump()).encode("utf-8")
            ).hexdigest()

            if genome_id not in seen_node_ids:
                seen_node_ids.add(genome_id)
                node = BioCypherNode(
                    node_id=genome_id,
                    preferred_id=f"reference_genome_{i}",
                    node_label="genome",
                    properties={
                        "species": data.reference.reference_genome.species,
                        "strain": data.reference.reference_genome.strain,
                        "serialized_data": json.dumps(
                            data.reference.reference_genome.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_experiment_nodes(self) -> None:
        nodes = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()

            node = BioCypherNode(
                node_id=experiment_id,
                preferred_id=f"DmfKuzmin2018_{i}",
                node_label="experiment",
                properties={
                    "dataset_index": i,
                    "serialized_data": json.dumps(data["experiment"].model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_genotype_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            for genotype in data["experiment"].genotype:
                genotype_id = hashlib.md5(
                    json.dumps(genotype.model_dump()).encode("utf-8")
                ).hexdigest()

                if genotype_id not in seen_node_ids:
                    seen_node_ids.add(genotype_id)
                    systematic_gene_name = genotype.perturbation.systematic_gene_name
                    perturbed_gene_name = genotype.perturbation.perturbed_gene_name
                    description = genotype.perturbation.description
                    perturbation_type = genotype.perturbation.perturbation_type
                    self._get_perturbation(genotype)

                    node = BioCypherNode(
                        node_id=genotype_id,
                        preferred_id=f"genotype_{i}",
                        node_label="genotype",
                        properties={
                            "systematic_gene_names": [systematic_gene_name],
                            "perturbed_gene_names": [perturbed_gene_name],
                            "is_deletion_genotype": isinstance(
                                data["experiment"].genotype, Genotype
                            ),
                            "is_interference_genotype": isinstance(
                                data["experiment"].genotype, Genotype
                            ),
                            "description": description,
                            "perturbation_types": [perturbation_type],
                            "serialized_data": json.dumps(genotype.model_dump()),
                        },
                    )
                    nodes.append(node)
        return nodes

    @staticmethod
    def _get_perturbation(
        genotype: Genotype,
    ) -> Generator[BioCypherNode, None, None]:
        nodes = []
        if genotype.perturbation:
            i = 1
            perturbation_id = hashlib.md5(
                json.dumps(genotype.perturbation.model_dump()).encode("utf-8")
            ).hexdigest()

            node = BioCypherNode(
                node_id=perturbation_id,
                preferred_id=f"perturbation_{i}",
                node_label="perturbation",
                properties={
                    "systematic_gene_name": [
                        genotype.perturbation.systematic_gene_name
                    ],
                    "perturbed_gene_name": [genotype.perturbation.perturbed_gene_name],
                    "description": genotype.perturbation.description,
                    "perturbation_type": genotype.perturbation.perturbation_type,
                    "strain_id": genotype.perturbation.strain_id,
                    "serialized_data": json.dumps(genotype.perturbation.model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_environment_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()

            node_id = environment_id

            if node_id not in seen_node_ids:
                seen_node_ids.add(node_id)
                media = json.dumps(data["experiment"].environment.media.model_dump())

                node = BioCypherNode(
                    node_id=node_id,
                    preferred_id=f"environment_{i}",
                    node_label="environment",
                    properties={
                        "temperature": data["experiment"].environment.temperature.value,
                        "media": media,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["reference"].reference_environment.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            node_id = environment_id

            if node_id not in seen_node_ids:
                seen_node_ids.add(node_id)
                media = json.dumps(
                    data["reference"].reference_environment.media.model_dump()
                )

                node = BioCypherNode(
                    node_id=node_id,
                    preferred_id=f"environment_{i}",
                    node_label="environment",
                    properties={
                        "temperature": data[
                            "reference"
                        ].reference_environment.temperature.value,
                        "media": media,
                        "serialized_data": json.dumps(
                            data["reference"].reference_environment.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_media_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            media_id = hashlib.md5(
                json.dumps(data["experiment"].environment.media.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            if media_id not in seen_node_ids:
                seen_node_ids.add(media_id)
                name = data["experiment"].environment.media.name
                state = data["experiment"].environment.media.state

                node = BioCypherNode(
                    node_id=media_id,
                    preferred_id=f"media_{media_id}",
                    node_label="media",
                    properties={
                        "name": name,
                        "state": state,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.media.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        for i, data in tqdm(enumerate(self.dataset)):
            media_id = hashlib.md5(
                json.dumps(
                    data["reference"].reference_environment.media.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if media_id not in seen_node_ids:
                seen_node_ids.add(media_id)
                name = data["reference"].reference_environment.media.name
                state = data["reference"].reference_environment.media.state

                node = BioCypherNode(
                    node_id=media_id,
                    preferred_id=f"media_{media_id}",
                    node_label="media",
                    properties={
                        "name": name,
                        "state": state,
                        "serialized_data": json.dumps(
                            data["reference"].reference_environment.media.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_temperature_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            temperature_id = hashlib.md5(
                json.dumps(
                    data["experiment"].environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if temperature_id not in seen_node_ids:
                seen_node_ids.add(temperature_id)

                node = BioCypherNode(
                    node_id=temperature_id,
                    preferred_id=f"temperature_{temperature_id}",
                    node_label="temperature",
                    properties={
                        "value": data["experiment"].environment.temperature.value,
                        "unit": data["experiment"].environment.temperature.unit,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.temperature.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        for i, data in tqdm(enumerate(self.dataset)):
            temperature_id = hashlib.md5(
                json.dumps(
                    data["reference"].reference_environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if temperature_id not in seen_node_ids:
                seen_node_ids.add(temperature_id)

                node = BioCypherNode(
                    node_id=temperature_id,
                    preferred_id=f"temperature_{temperature_id}",
                    node_label="temperature",
                    properties={
                        "value": data[
                            "reference"
                        ].reference_environment.temperature.value,
                        "description": data[
                            "reference"
                        ].reference_environment.temperature.description,
                        "serialized_data": json.dumps(
                            data[
                                "reference"
                            ].reference_environment.temperature.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_phenotype_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            phenotype_id = hashlib.md5(
                json.dumps(data["experiment"].phenotype.model_dump()).encode("utf-8")
            ).hexdigest()

            if phenotype_id not in seen_node_ids:
                seen_node_ids.add(phenotype_id)
                graph_level = data["experiment"].phenotype.graph_level
                label = data["experiment"].phenotype.label
                label_error = data["experiment"].phenotype.label_error
                fitness = data["experiment"].phenotype.fitness
                fitness_std = data["experiment"].phenotype.fitness_std

                node = BioCypherNode(
                    node_id=phenotype_id,
                    preferred_id=f"phenotype_{phenotype_id}",
                    node_label="phenotype",
                    properties={
                        "graph_level": graph_level,
                        "label": label,
                        "label_error": label_error,
                        "fitness": fitness,
                        "fitness_std": fitness_std,
                        "serialized_data": json.dumps(
                            data["experiment"].phenotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        # References
        for i, data in tqdm(enumerate(self.dataset)):
            # Get the phenotype ID associated with the experiment reference
            phenotype_id = hashlib.md5(
                json.dumps(data["reference"].reference_phenotype.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            if phenotype_id not in seen_node_ids:
                seen_node_ids.add(phenotype_id)
                graph_level = data["reference"].reference_phenotype.graph_level
                label = data["reference"].reference_phenotype.label
                label_error = data["reference"].reference_phenotype.label_error
                fitness = data["reference"].reference_phenotype.fitness
                fitness_std = data["reference"].reference_phenotype.fitness_std

                node = BioCypherNode(
                    node_id=phenotype_id,
                    preferred_id=f"phenotype_{phenotype_id}",
                    node_label="phenotype",
                    properties={
                        "graph_level": graph_level,
                        "label": label,
                        "label_error": label_error,
                        "fitness": fitness,
                        "fitness_std": fitness_std,
                        "serialized_data": json.dumps(
                            data["reference"].reference_phenotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_dataset_nodes(self) -> None:
        nodes = [
            BioCypherNode(
                node_id="DmfKuzmin2018",
                preferred_id="DmfKuzmin2018",
                node_label="dataset",
            )
        ]
        return nodes

    def get_edges(self):
        methods = [
            self._get_dataset_experiment_ref_edges,
            self._get_experiment_dataset_edges,
            self._get_experiment_ref_experiment_edges,
            self._get_genotype_experiment_edges,
            self._get_environment_experiment_edges,
            self._get_environment_experiment_ref_edges,
            self._get_phenotype_experiment_edges,
            self._get_phenotype_experiment_ref_edges,
            self._get_media_environment_edges,
            self._get_temperature_environment_edges,
            self._get_genome_edges,
        ]

        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(method) for method in methods]
            for future in as_completed(futures):
                try:
                    edge_generator = future.result()
                    for edge in edge_generator:
                        yield edge
                except Exception as exc:
                    logger.error(
                        f"Edge generation method generated an exception: {exc}"
                    )

    def _get_dataset_experiment_ref_edges(self):
        edges = []
        for data in self.dataset.experiment_reference_index:
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            edge = BioCypherEdge(
                source_id=experiment_ref_id,
                target_id="DmfKuzmin2018",
                relationship_label="experiment reference member of",
            )
            edges.append(edge)
        return edges

    def _get_experiment_dataset_edges(self):
        # concept level
        edges = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            edge = BioCypherEdge(
                source_id=experiment_id,
                target_id="DmfKuzmin2018",
                relationship_label="experiment member of",
            )
            edges.append(edge)
        return edges

    def _get_experiment_ref_experiment_edges(self):
        # instance level
        edges = []
        for data in tqdm(self.dataset.experiment_reference_index):
            dataset_subset = self.dataset[torch.tensor(data.index)]
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            for i, data in enumerate(dataset_subset):
                experiment_id = hashlib.md5(
                    json.dumps(data["experiment"].model_dump()).encode("utf-8")
                ).hexdigest()
                edge = BioCypherEdge(
                    source_id=experiment_ref_id,
                    target_id=experiment_id,
                    relationship_label="experiment reference of",
                )
                edges.append(edge)
        return edges

    def _get_genotype_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        # CHECK if needed - don't think needed since exp ref index
        # seen_genotype_experiment_pairs: Set[tuple] = set()
        edges = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            for genotype in data["experiment"].genotype:
                genotype_id = hashlib.md5(
                    json.dumps(genotype.model_dump()).encode("utf-8")
                ).hexdigest()

                self._get_perturbation_genotype_edges(
                    genotype=genotype, genotype_id=genotype_id
                )

                # CHECK if needed - don't think needed since exp ref index
                # genotype_experiment_pair = (genotype_id, experiment_id)
                # if genotype_experiment_pair not in seen_genotype_experiment_pairs:
                #     seen_genotype_experiment_pairs.add(genotype_experiment_pair)

                edge = BioCypherEdge(
                    source_id=genotype_id,
                    target_id=experiment_id,
                    relationship_label="genotype member of",
                )
                edges.append(edge)
        return edges

    @staticmethod
    def _get_perturbation_genotype_edges(
        genotype: Genotype, genotype_id: str
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        if genotype.perturbation:
            perturbation_id = hashlib.md5(
                json.dumps(genotype.perturbation.model_dump()).encode("utf-8")
            ).hexdigest()

            edge = BioCypherEdge(
                source_id=perturbation_id,
                target_id=genotype_id,
                relationship_label="perturbation member of",
            )
            edges.append(edge)
        return edges

    def _get_environment_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_environment_experiment_pairs: Set[tuple] = set()
        # Linking environments to experiments
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()

            env_experiment_pair = (environment_id, experiment_id)
            if env_experiment_pair not in seen_environment_experiment_pairs:
                seen_environment_experiment_pairs.add(env_experiment_pair)
                edge = BioCypherEdge(
                    source_id=environment_id,
                    target_id=experiment_id,
                    relationship_label="environment member of",
                )
                edges.append(edge)
        return edges

    def _get_environment_experiment_ref_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_environment_experiment_ref_pairs: Set[tuple] = set()
        # Linking environments to experiment references
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            environment_id = hashlib.md5(
                json.dumps(data.reference.reference_environment.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            env_experiment_ref_pair = (environment_id, experiment_ref_id)
            if env_experiment_ref_pair not in seen_environment_experiment_ref_pairs:
                seen_environment_experiment_ref_pairs.add(env_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=environment_id,
                    target_id=experiment_ref_id,
                    relationship_label="environment member of",
                )
                edges.append(edge)
        return edges

    def _get_phenotype_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_phenotype_experiment_pairs: Set[tuple] = set()
        # Linking phenotypes to experiments
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            phenotype_id = hashlib.md5(
                json.dumps(data["experiment"].phenotype.model_dump()).encode("utf-8")
            ).hexdigest()

            phenotype_experiment_pair = (phenotype_id, experiment_id)
            if phenotype_experiment_pair not in seen_phenotype_experiment_pairs:
                seen_phenotype_experiment_pairs.add(phenotype_experiment_pair)

                edge = BioCypherEdge(
                    source_id=phenotype_id,
                    target_id=experiment_id,
                    relationship_label="phenotype member of",
                )
                edges.append(edge)
        return edges

    def _get_phenotype_experiment_ref_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_phenotype_experiment_ref_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            phenotype_id = hashlib.md5(
                json.dumps(data.reference.reference_phenotype.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            phenotype_experiment_ref_pair = (phenotype_id, experiment_ref_id)
            if phenotype_experiment_ref_pair not in seen_phenotype_experiment_ref_pairs:
                seen_phenotype_experiment_ref_pairs.add(phenotype_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=phenotype_id,
                    target_id=experiment_ref_id,
                    relationship_label="phenotype member of",
                )
                edges.append(edge)
        return edges

    def _get_media_environment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_media_environment_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()
            media_id = hashlib.md5(
                json.dumps(data["experiment"].environment.media.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            media_environment_pair = (media_id, environment_id)
            if media_environment_pair not in seen_media_environment_pairs:
                seen_media_environment_pairs.add(media_environment_pair)

                edge = BioCypherEdge(
                    source_id=media_id,
                    target_id=environment_id,
                    relationship_label="media member of",
                )
                edges.append(edge)
        return edges

    def _get_temperature_environment_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_temperature_environment_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()
            temperature_id = hashlib.md5(
                json.dumps(
                    data["experiment"].environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            temperature_environment_pair = (temperature_id, environment_id)
            if temperature_environment_pair not in seen_temperature_environment_pairs:
                seen_temperature_environment_pairs.add(temperature_environment_pair)

                edge = BioCypherEdge(
                    source_id=temperature_id,
                    target_id=environment_id,
                    relationship_label="temperature member of",
                )
                edges.append(edge)
        return edges

    def _get_genome_edges(self) -> None:
        edges = []
        seen_genome_experiment_ref_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            genome_id = hashlib.md5(
                json.dumps(data.reference.reference_genome.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            genome_experiment_ref_pair = (genome_id, experiment_ref_id)
            if genome_experiment_ref_pair not in seen_genome_experiment_ref_pairs:
                seen_genome_experiment_ref_pairs.add(genome_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=genome_id,
                    target_id=experiment_ref_id,
                    relationship_label="genome member of",
                )
                edges.append(edge)
        return edges


class TmfKuzmin2018Adapter:
    def __init__(self, dataset: TmfKuzmin2018Dataset, num_workers: int):
        self.dataset = dataset
        self.num_workers = num_workers

    def get_nodes(self):
        methods = [
            self._get_experiment_reference_nodes,
            self._get_genome_nodes,
            self._get_experiment_nodes,
            self._get_dataset_nodes,
            self._get_genotype_nodes,
            self._get_environment_nodes,
            self._get_media_nodes,
            self._get_temperature_nodes,
            self._get_phenotype_nodes,
        ]

        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(method) for method in methods]

            for future in as_completed(futures):
                try:
                    node_generator = future.result()
                    for node in node_generator:
                        yield node
                except Exception as exc:
                    logger.error(
                        f"Node generation method generated an exception: {exc}"
                    )

    def _get_experiment_reference_nodes(self) -> None:
        nodes = []
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            node = BioCypherNode(
                node_id=experiment_ref_id,
                preferred_id=f"TmfKuzmin2018_reference_{i}",
                node_label="experiment reference",
                properties={
                    "dataset_index": i,
                    "serialized_data": json.dumps(data.reference.model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_genome_nodes(self) -> None:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            genome_id = hashlib.md5(
                json.dumps(data.reference.reference_genome.model_dump()).encode("utf-8")
            ).hexdigest()

            if genome_id not in seen_node_ids:
                seen_node_ids.add(genome_id)
                node = BioCypherNode(
                    node_id=genome_id,
                    preferred_id=f"reference_genome_{i}",
                    node_label="genome",
                    properties={
                        "species": data.reference.reference_genome.species,
                        "strain": data.reference.reference_genome.strain,
                        "serialized_data": json.dumps(
                            data.reference.reference_genome.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_experiment_nodes(self) -> None:
        nodes = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            node = BioCypherNode(
                node_id=experiment_id,
                preferred_id=f"TmfKuzmin2018_{i}",
                node_label="experiment",
                properties={
                    "dataset_index": i,
                    "serialized_data": json.dumps(data["experiment"].model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_genotype_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            for genotype in data["experiment"].genotype:
                genotype_id = hashlib.md5(
                    json.dumps(genotype.model_dump()).encode("utf-8")
                ).hexdigest()

                if genotype_id not in seen_node_ids:
                    seen_node_ids.add(genotype_id)
                    systematic_gene_name = genotype.perturbation.systematic_gene_name
                    perturbed_gene_name = genotype.perturbation.perturbed_gene_name
                    description = genotype.perturbation.description
                    perturbation_type = genotype.perturbation.perturbation_type
                    self._get_perturbation(genotype)

                    node = BioCypherNode(
                        node_id=genotype_id,
                        preferred_id=f"genotype_{i}",
                        node_label="genotype",
                        properties={
                            "systematic_gene_names": [systematic_gene_name],
                            "perturbed_gene_names": [perturbed_gene_name],
                            "is_deletion_genotype": isinstance(
                                data["experiment"].genotype, Genotype
                            ),
                            "is_interference_genotype": isinstance(
                                data["experiment"].genotype, Genotype
                            ),
                            "description": description,
                            "perturbation_types": [perturbation_type],
                            "serialized_data": json.dumps(genotype.model_dump()),
                        },
                    )
                    nodes.append(node)
        return nodes

    @staticmethod
    def _get_perturbation(
        genotype: Genotype,
    ) -> Generator[BioCypherNode, None, None]:
        nodes = []
        if genotype.perturbation:
            i = 1
            perturbation_id = hashlib.md5(
                json.dumps(genotype.perturbation.model_dump()).encode("utf-8")
            ).hexdigest()

            node = BioCypherNode(
                node_id=perturbation_id,
                preferred_id=f"perturbation_{i}",
                node_label="perturbation",
                properties={
                    "systematic_gene_name": [
                        genotype.perturbation.systematic_gene_name
                    ],
                    "perturbed_gene_name": [genotype.perturbation.perturbed_gene_name],
                    "description": genotype.perturbation.description,
                    "perturbation_type": genotype.perturbation.perturbation_type,
                    "strain_id": genotype.perturbation.strain_id,
                    "serialized_data": json.dumps(genotype.perturbation.model_dump()),
                },
            )
            nodes.append(node)
        return nodes

    def _get_environment_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()

            node_id = environment_id

            if node_id not in seen_node_ids:
                seen_node_ids.add(node_id)
                media = json.dumps(data["experiment"].environment.media.model_dump())

                node = BioCypherNode(
                    node_id=node_id,
                    preferred_id=f"environment_{i}",
                    node_label="environment",
                    properties={
                        "temperature": data["experiment"].environment.temperature.value,
                        "media": media,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["reference"].reference_environment.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            node_id = environment_id

            if node_id not in seen_node_ids:
                seen_node_ids.add(node_id)
                media = json.dumps(
                    data["reference"].reference_environment.media.model_dump()
                )

                node = BioCypherNode(
                    node_id=node_id,
                    preferred_id=f"environment_{i}",
                    node_label="environment",
                    properties={
                        "temperature": data[
                            "reference"
                        ].reference_environment.temperature.value,
                        "media": media,
                        "serialized_data": json.dumps(
                            data["reference"].reference_environment.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_media_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            media_id = hashlib.md5(
                json.dumps(data["experiment"].environment.media.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            if media_id not in seen_node_ids:
                seen_node_ids.add(media_id)
                name = data["experiment"].environment.media.name
                state = data["experiment"].environment.media.state

                node = BioCypherNode(
                    node_id=media_id,
                    preferred_id=f"media_{media_id}",
                    node_label="media",
                    properties={
                        "name": name,
                        "state": state,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.media.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        for i, data in tqdm(enumerate(self.dataset)):
            media_id = hashlib.md5(
                json.dumps(
                    data["reference"].reference_environment.media.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if media_id not in seen_node_ids:
                seen_node_ids.add(media_id)
                name = data["reference"].reference_environment.media.name
                state = data["reference"].reference_environment.media.state

                node = BioCypherNode(
                    node_id=media_id,
                    preferred_id=f"media_{media_id}",
                    node_label="media",
                    properties={
                        "name": name,
                        "state": state,
                        "serialized_data": json.dumps(
                            data["reference"].reference_environment.media.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_temperature_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            temperature_id = hashlib.md5(
                json.dumps(
                    data["experiment"].environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if temperature_id not in seen_node_ids:
                seen_node_ids.add(temperature_id)

                node = BioCypherNode(
                    node_id=temperature_id,
                    preferred_id=f"temperature_{temperature_id}",
                    node_label="temperature",
                    properties={
                        "value": data["experiment"].environment.temperature.value,
                        "unit": data["experiment"].environment.temperature.unit,
                        "serialized_data": json.dumps(
                            data["experiment"].environment.temperature.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        for i, data in tqdm(enumerate(self.dataset)):
            temperature_id = hashlib.md5(
                json.dumps(
                    data["reference"].reference_environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            if temperature_id not in seen_node_ids:
                seen_node_ids.add(temperature_id)

                node = BioCypherNode(
                    node_id=temperature_id,
                    preferred_id=f"temperature_{temperature_id}",
                    node_label="temperature",
                    properties={
                        "value": data[
                            "reference"
                        ].reference_environment.temperature.value,
                        "description": data[
                            "reference"
                        ].reference_environment.temperature.description,
                        "serialized_data": json.dumps(
                            data[
                                "reference"
                            ].reference_environment.temperature.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_phenotype_nodes(self) -> Generator[BioCypherNode, None, None]:
        nodes = []
        seen_node_ids: Set[str] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            phenotype_id = hashlib.md5(
                json.dumps(data["experiment"].phenotype.model_dump()).encode("utf-8")
            ).hexdigest()

            if phenotype_id not in seen_node_ids:
                seen_node_ids.add(phenotype_id)
                graph_level = data["experiment"].phenotype.graph_level
                label = data["experiment"].phenotype.label
                label_error = data["experiment"].phenotype.label_error
                fitness = data["experiment"].phenotype.fitness
                fitness_std = data["experiment"].phenotype.fitness_std

                node = BioCypherNode(
                    node_id=phenotype_id,
                    preferred_id=f"phenotype_{phenotype_id}",
                    node_label="phenotype",
                    properties={
                        "graph_level": graph_level,
                        "label": label,
                        "label_error": label_error,
                        "fitness": fitness,
                        "fitness_std": fitness_std,
                        "serialized_data": json.dumps(
                            data["experiment"].phenotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)

        # References
        for i, data in tqdm(enumerate(self.dataset)):
            # Get the phenotype ID associated with the experiment reference
            phenotype_id = hashlib.md5(
                json.dumps(data["reference"].reference_phenotype.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            if phenotype_id not in seen_node_ids:
                seen_node_ids.add(phenotype_id)
                graph_level = data["reference"].reference_phenotype.graph_level
                label = data["reference"].reference_phenotype.label
                label_error = data["reference"].reference_phenotype.label_error
                fitness = data["reference"].reference_phenotype.fitness
                fitness_std = data["reference"].reference_phenotype.fitness_std

                node = BioCypherNode(
                    node_id=phenotype_id,
                    preferred_id=f"phenotype_{phenotype_id}",
                    node_label="phenotype",
                    properties={
                        "graph_level": graph_level,
                        "label": label,
                        "label_error": label_error,
                        "fitness": fitness,
                        "fitness_std": fitness_std,
                        "serialized_data": json.dumps(
                            data["reference"].reference_phenotype.model_dump()
                        ),
                    },
                )
                nodes.append(node)
        return nodes

    def _get_dataset_nodes(self) -> None:
        nodes = [
            BioCypherNode(
                node_id="TmfKuzmin2018",
                preferred_id="TmfKuzmin2018",
                node_label="dataset",
            )
        ]
        return nodes

    def get_edges(self):
        methods = [
            self._get_dataset_experiment_ref_edges,
            self._get_experiment_dataset_edges,
            self._get_experiment_ref_experiment_edges,
            self._get_genotype_experiment_edges,
            self._get_environment_experiment_edges,
            self._get_environment_experiment_ref_edges,
            self._get_phenotype_experiment_edges,
            self._get_phenotype_experiment_ref_edges,
            self._get_media_environment_edges,
            self._get_temperature_environment_edges,
            self._get_genome_edges,
        ]

        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(method) for method in methods]
            for future in as_completed(futures):
                try:
                    edge_generator = future.result()
                    for edge in edge_generator:
                        yield edge
                except Exception as exc:
                    logger.error(
                        f"Edge generation method generated an exception: {exc}"
                    )

    def _get_dataset_experiment_ref_edges(self):
        edges = []
        for data in self.dataset.experiment_reference_index:
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            edge = BioCypherEdge(
                source_id=experiment_ref_id,
                target_id="TmfKuzmin2018",
                relationship_label="experiment reference member of",
            )
            edges.append(edge)
        return edges

    def _get_experiment_dataset_edges(self):
        edges = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            edge = BioCypherEdge(
                source_id=experiment_id,
                target_id="TmfKuzmin2018",
                relationship_label="experiment member of",
            )
            edges.append(edge)
        return edges

    def _get_experiment_ref_experiment_edges(self):
        edges = []
        for data in tqdm(self.dataset.experiment_reference_index):
            dataset_subset = self.dataset[torch.tensor(data.index)]
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()
            for i, data in enumerate(dataset_subset):
                experiment_id = hashlib.md5(
                    json.dumps(data["experiment"].model_dump()).encode("utf-8")
                ).hexdigest()
                edge = BioCypherEdge(
                    source_id=experiment_ref_id,
                    target_id=experiment_id,
                    relationship_label="experiment reference of",
                )
                edges.append(edge)
        return edges

    def _get_genotype_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        # CHECK if needed - don't think needed since exp ref index
        # seen_genotype_experiment_pairs: Set[tuple] = set()
        edges = []
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            for genotype in data["experiment"].genotype:
                genotype_id = hashlib.md5(
                    json.dumps(genotype.model_dump()).encode("utf-8")
                ).hexdigest()

                self._get_perturbation_genotype_edges(
                    genotype=genotype, genotype_id=genotype_id
                )

                # CHECK if needed - don't think needed since exp ref index
                # genotype_experiment_pair = (genotype_id, experiment_id)
                # if genotype_experiment_pair not in seen_genotype_experiment_pairs:
                #     seen_genotype_experiment_pairs.add(genotype_experiment_pair)

                edge = BioCypherEdge(
                    source_id=genotype_id,
                    target_id=experiment_id,
                    relationship_label="genotype member of",
                )
                edges.append(edge)

    @staticmethod
    def _get_perturbation_genotype_edges(
        genotype: Genotype, genotype_id: str
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        if genotype.perturbation:
            perturbation_id = hashlib.md5(
                json.dumps(genotype.perturbation.model_dump()).encode("utf-8")
            ).hexdigest()

            edge = BioCypherEdge(
                source_id=perturbation_id,
                target_id=genotype_id,
                relationship_label="perturbation member of",
            )
            edges.append(edge)
        return edges

    def _get_environment_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_environment_experiment_pairs: Set[tuple] = set()
        # Linking environments to experiments
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()

            env_experiment_pair = (environment_id, experiment_id)
            if env_experiment_pair not in seen_environment_experiment_pairs:
                seen_environment_experiment_pairs.add(env_experiment_pair)

                edge = BioCypherEdge(
                    source_id=environment_id,
                    target_id=experiment_id,
                    relationship_label="environment member of",
                )
                edges.append(edge)
        return edges

    def _get_environment_experiment_ref_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_environment_experiment_ref_pairs: Set[tuple] = set()
        # Linking environments to experiment references
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            environment_id = hashlib.md5(
                json.dumps(data.reference.reference_environment.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            env_experiment_ref_pair = (environment_id, experiment_ref_id)
            if env_experiment_ref_pair not in seen_environment_experiment_ref_pairs:
                seen_environment_experiment_ref_pairs.add(env_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=environment_id,
                    target_id=experiment_ref_id,
                    relationship_label="environment member of",
                )
                edges.append(edge)
        return edges

    def _get_phenotype_experiment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_phenotype_experiment_pairs: Set[tuple] = set()
        # Linking phenotypes to experiments
        for i, data in tqdm(enumerate(self.dataset)):
            experiment_id = hashlib.md5(
                json.dumps(data["experiment"].model_dump()).encode("utf-8")
            ).hexdigest()
            phenotype_id = hashlib.md5(
                json.dumps(data["experiment"].phenotype.model_dump()).encode("utf-8")
            ).hexdigest()

            phenotype_experiment_pair = (phenotype_id, experiment_id)
            if phenotype_experiment_pair not in seen_phenotype_experiment_pairs:
                seen_phenotype_experiment_pairs.add(phenotype_experiment_pair)

                edge = BioCypherEdge(
                    source_id=phenotype_id,
                    target_id=experiment_id,
                    relationship_label="phenotype member of",
                )
                edges.append(edge)
        return edges

    def _get_phenotype_experiment_ref_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_phenotype_experiment_ref_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            phenotype_id = hashlib.md5(
                json.dumps(data.reference.reference_phenotype.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            phenotype_experiment_ref_pair = (phenotype_id, experiment_ref_id)
            if phenotype_experiment_ref_pair not in seen_phenotype_experiment_ref_pairs:
                seen_phenotype_experiment_ref_pairs.add(phenotype_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=phenotype_id,
                    target_id=experiment_ref_id,
                    relationship_label="phenotype member of",
                )
                edges.append(edge)
        return edges

    def _get_media_environment_edges(self) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_media_environment_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()
            media_id = hashlib.md5(
                json.dumps(data["experiment"].environment.media.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            media_environment_pair = (media_id, environment_id)
            if media_environment_pair not in seen_media_environment_pairs:
                seen_media_environment_pairs.add(media_environment_pair)

                edge = BioCypherEdge(
                    source_id=media_id,
                    target_id=environment_id,
                    relationship_label="media member of",
                )
                edges.append(edge)
        return edges

    def _get_temperature_environment_edges(
        self,
    ) -> Generator[BioCypherEdge, None, None]:
        edges = []
        seen_temperature_environment_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset)):
            environment_id = hashlib.md5(
                json.dumps(data["experiment"].environment.model_dump()).encode("utf-8")
            ).hexdigest()
            temperature_id = hashlib.md5(
                json.dumps(
                    data["experiment"].environment.temperature.model_dump()
                ).encode("utf-8")
            ).hexdigest()

            temperature_environment_pair = (temperature_id, environment_id)
            if temperature_environment_pair not in seen_temperature_environment_pairs:
                seen_temperature_environment_pairs.add(temperature_environment_pair)

                edge = BioCypherEdge(
                    source_id=temperature_id,
                    target_id=environment_id,
                    relationship_label="temperature member of",
                )
                edges.append(edge)
        return edges

    def _get_genome_edges(self) -> None:
        edges = []
        seen_genome_experiment_ref_pairs: Set[tuple] = set()
        for i, data in tqdm(enumerate(self.dataset.experiment_reference_index)):
            experiment_ref_id = hashlib.md5(
                json.dumps(data.reference.model_dump()).encode("utf-8")
            ).hexdigest()

            genome_id = hashlib.md5(
                json.dumps(data.reference.reference_genome.model_dump()).encode(
                    "utf-8"
                )
            ).hexdigest()

            genome_experiment_ref_pair = (genome_id, experiment_ref_id)
            if genome_experiment_ref_pair not in seen_genome_experiment_ref_pairs:
                seen_genome_experiment_ref_pairs.add(genome_experiment_ref_pair)

                edge = BioCypherEdge(
                    source_id=genome_id,
                    target_id=experiment_ref_id,
                    relationship_label="genome member of",
                )
                edges.append(edge)
        return edges


if __name__ == "__main__":
    from biocypher import BioCypher

    ## Smf
    # Simple Testing
    dataset = SmfKuzmin2018Dataset()
    adapter = SmfKuzmin2018Adapter(dataset=dataset, num_workers=1)
    [i for i in adapter.get_nodes()]
    [i for i in adapter.get_edges()]

    # # Advanced Testing
    # bc = BioCypher()
    # dataset = SmfKuzmin2018Dataset()
    # adapter = SmfKuzmin2018Adapter(dataset=dataset, num_workers=10)
    # print(bc.show_ontology_structure())
    # bc.write_nodes(adapter.get_nodes())
    # # bc.write_edges(adapter.get_edges())
    # bc.write_import_call()
    # bc.write_schema_info(as_node=True)
    # bc.summary()

    ## Dmf
    # Simple Testing
    dataset = DmfKuzmin2018Dataset()
    adapter = DmfKuzmin2018Adapter(dataset=dataset)
    [i for i in adapter.get_nodes()]
    [i for i in adapter.get_edges()]

    # # Advanced Testing
    # bc = BioCypher()
    # dataset = DmfKuzmin2018Dataset()
    # adapter = DmfKuzmin2018Adapter(dataset=dataset, num_workers=10)
    # print(bc.show_ontology_structure())
    # bc.write_nodes(adapter.get_nodes())
    # bc.write_edges(adapter.get_edges())
    # bc.write_import_call()
    # bc.write_schema_info(as_node=True)
    # bc.summary()
    # print()

    ## Tmf
    # Simple Testing
    dataset = TmfKuzmin2018Dataset()
    adapter = TmfKuzmin2018Adapter(dataset=dataset)
    [i for i in adapter.get_nodes()]
    [i for i in adapter.get_edges()]

    # # Advanced Testing
    # bc = BioCypher()
    # dataset = TmfKuzmin2018Dataset()
    # adapter = TmfKuzmin2018Adapter(dataset=dataset, num_workers=10)
    # bc.show_ontology_structure()
    # bc.write_nodes(adapter.get_nodes())
    # bc.write_edges(adapter.get_edges())
    # bc.write_import_call()
    # bc.write_schema_info(as_node=True)
    # bc.summary()
    # print()
