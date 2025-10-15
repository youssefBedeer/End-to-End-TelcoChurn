from src import logging, CustomException 

from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline 
from src.pipeline.stage_02_data_validation import DataValidationPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    data_ingestion = DataIngestionPipeline() 
    data_ingestion.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)



STAGE_NAME = "Data Validation stage"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    data_validation = DataValidationPipeline() 
    data_validation.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)



STAGE_NAME = "Data Transformation stage"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    data_transformation = DataTransformationPipeline() 
    data_transformation.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)



