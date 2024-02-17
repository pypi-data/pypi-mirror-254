from functools import cached_property

from datasets import Dataset
from datasets.fingerprint import Hasher

from ..step_operations import _INTERNAL_STEP_OPERATION_KEY
from .data_source import DataSource


class HFDatasetDataSource(DataSource):
    def __init__(
        self,
        name: str,
        dataset_path: str,
        progress_interval: None | int = None,
        force: bool = False,
        verbose: None | bool = None,
        log_level: None | int = None,
        save_num_proc: None | int = None,
        save_num_shards: None | int = None,
        background: bool = False,
    ):
        self.path_to_dataset = dataset_path
        super().__init__(
            name,
            data=None,  # type: ignore[arg-type]
            progress_interval=progress_interval,
            force=force,
            verbose=verbose,
            log_level=log_level,
            save_num_proc=save_num_proc,
            save_num_shards=save_num_shards,
            background=background,
        )

    def setup(self):
        pass

    def run(self):
        return Dataset.load_from_disk(self.path_to_dataset)

    @cached_property
    def fingerprint(self) -> str:
        return Hasher.hash([super().fingerprint, self.path_to_dataset])


setattr(HFDatasetDataSource, _INTERNAL_STEP_OPERATION_KEY, True)

__all__ = ["HFDatasetDataSource"]
