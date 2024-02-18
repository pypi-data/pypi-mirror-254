from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file_train: Path
    local_data_file_test:Path
    unzip_dir: Path

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    data_dir:Path
    updated_base_model_path: Path
    model_param_file:Path
    target_column:str
    drop_column:list
    test_train_split:int
    random_state:int