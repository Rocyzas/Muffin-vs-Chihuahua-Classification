import time
from src.cnnClassifier import logger
from tracemalloc import start
from cnnClassifier.pipeline.stage_03_training_model import TrainingModelPipeline
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    start_time = time.time()
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    logger.info(f"Elapsed Time: {int(time.time() - start_time)}s")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare Base Model stage"


try:
    start_time = time.time()
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = PrepareBaseModelPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    logger.info(f"Elapsed Time: {int(time.time() - start_time)}s")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Train Model stage"


try:
    start_time = time.time()
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = TrainingModelPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    logger.info(f"Elapsed Time: {int(time.time() - start_time)}s")

except Exception as e:
        logger.exception(e)
        raise e