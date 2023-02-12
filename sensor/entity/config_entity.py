import os
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime


_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(), "artifact",f"{datetime.now().strftime('%m%d%Y_%H%M%S')}")

class DataInjestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="aps"
            self.collection_name="sensor"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_dir=os.path.join(self.data_ingestion_dir,"feature_store")
            self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size=0.2
        except Exception as e:
            raise SensorException(e, SystemExit())

    def to_dict()->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)
