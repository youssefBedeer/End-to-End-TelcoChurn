from src import logging, CustomException 

from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline 

STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} started {'<'*20}\n")
    data_ingestion = DataIngestionPipeline() 
    data_ingestion.main()
    logging.info(f"\n{'>'*20} stage {STAGE_NAME} completed {'<'*20}\n")

except Exception as e:
    raise CustomException(e)