import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client

def get_collection_as_dataframe(databse_name:str, collection_name:str) -> pd.Dataframe:

    """
    This Function return collection as dataframe
    ============================================
    Params:
    database_name : database name
    collection-name: collection_name
    ============================================
    return Pandas dataframe of a collection
    
    """

    try:
        logging.info("Reading from database : {database_name} and Collectiom: {collection_name}")
        df = pd.Dataframe(list(mongo_client[databse_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info("Droping column: _id")
            df = df.drop("_id", axis=1)
        return df
    except Exception as e:
        raise SensorException(e, sys)
    