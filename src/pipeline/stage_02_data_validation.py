from src.config.configuration import ConfigurationManager 
from src.components.data_validation import DataValidation
from src import logging, CustomException 

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager() 
        data_validation_config = config.get_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()
        


STAGE_NAME = "Data Validation stage"

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e)