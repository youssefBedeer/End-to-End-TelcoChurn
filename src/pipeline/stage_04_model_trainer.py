
from src.components.model_trainer import ModelTrainer
from src.config.configuration import ConfigurationManager 
from src import logging, CustomException 

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager() 
        model_trainer_config=config.get_model_trainer()
        trainer = ModelTrainer(model_trainer_config) 
        trainer.get_best_params() 
        trainer.train()
        


STAGE_NAME = "Model Training stage"

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainer()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e)