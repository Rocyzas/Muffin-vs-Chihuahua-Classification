import time
from tracemalloc import start

from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    start_time = time.time()
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    logger.info(f"Elapsed Time: {int(time.time() - start)}s")

except Exception as e:
        logger.exception(e)
        raise e
