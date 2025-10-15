from src.constants import * 
from src.utils import read_yaml, create_directories 

from src.entity.config_entity import(DataIngestionConfig, DataTransformationConfig,
                                    DataValidationConfig,)




class ConfigurationManager:
    def __init__(self, 
                config_filepath:Path = Path(CONFIG_FILE_PATH),
                params_filepath:Path = Path(PARAMS_FILE_PATH),
                schema_filepath:Path = Path(SCHEMA_FILE_PATH)):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = str(config.source_url),
            local_data_file =  Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )
        
    
    
    def get_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation 
        schema = self.schema.COLUMNS 
        
        create_directories([config.root_dir])
        
        return DataValidationConfig(
            root_dir = Path(config.root_dir),
            STATUS_FILE = config.STATUS_FILE, 
            data_dir = Path(config.data_dir),
            all_schemas = schema   
        )
        
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        return DataTransformationConfig(
            root_dir= Path(config.root_dir),
            data_path=Path(config.data_path),
            transformer_path=Path(config.transformer_path),
            target_name= config.target_name,
            X_train_path=Path(config.X_train_path),
            X_test_path=Path(config.X_test_path),
            y_train_path=Path(config.y_train_path),
            y_test_path=Path(config.y_test_path)
        )