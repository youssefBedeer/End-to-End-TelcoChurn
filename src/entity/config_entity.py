from dataclasses import dataclass 
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: Path
  source_url: str
  local_data_file: Path 
  unzip_dir: Path
  
  
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str 
    data_dir: Path 
    all_schemas: dict
    
    
from dataclasses import dataclass 
from pathlib import Path 

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path
    transformer_path: Path
    target_name: str
    X_train_path: Path 
    X_test_path: Path 
    y_train_path: Path 
    y_test_path: Path
    
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path 
    model_name: str
    target_column: str 
    all_params:dict
    X_train_path : Path 
    X_test_path : Path
    y_train_path : Path
    y_test_path :Path
    THRESHOLD : float
    best_params_path : Path