from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, data_ingestion_config:config_entity.DataInjestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)
