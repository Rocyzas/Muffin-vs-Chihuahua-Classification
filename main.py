import argparse

import time
from src.cnnClassifier import logger
from tracemalloc import start
from cnnClassifier.pipeline.stage_03_training_model import TrainingModelPipeline
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_01B_data_preparation import DataPreparationPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_04_evaluation_model import EvaluateModelPipeline


parser = argparse.ArgumentParser(description='Run different stages of the pipeline.')

parser.add_argument('-ingest', action='store_true', help='Run the Data Ingestion stage')
parser.add_argument('-prepareData', action='store_true', help='Run the Data Preparation stage')
parser.add_argument('-prepareModel', action='store_true', help='Run the Prepare Base Model stage')
parser.add_argument('-train', action='store_true', help='Run the Train Model stage')
parser.add_argument('-evaluate', action='store_true', help='Run the Evaluate Model stage')

args = parser.parse_args()

if args.ingest:
    STAGE_NAME = "Data Ingestion stage"
    try:
        start_time = time.time()
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        logger.info(f"Elapsed Time: {int(time.time() - start_time)}s")

    except Exception as e:
            logger.exception(e)
            raise e

if args.prepareData:
    STAGE_NAME = "Data Preparation stage"
    try:
        start_time = time.time()
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataPreparationPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        logger.info(f"Elapsed Time: {int(time.time() - start_time)}s")

    except Exception as e:
            logger.exception(e)
            raise e

if args.prepareModel:
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

if args.train:
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

if args.evaluate:
    STAGE_NAME = "Model Evaluation stage"
    try:
        start_time = time.time()
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = EvaluateModelPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        logger.info(f"Elapsed Time: {int(time.time() - start_time)}s")

    except Exception as e:
            logger.exception(e)
            raise e