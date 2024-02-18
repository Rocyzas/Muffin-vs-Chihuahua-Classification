from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file_c: Path
    local_data_file_m: Path
    unzip_dir: Path
    num_chihuahua_files: int
    num_muffin_files: int
