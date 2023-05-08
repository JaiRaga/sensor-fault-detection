from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import sys
from dotenv import load_dotenv

load_dotenv()

def test_exception():
    try:
        logging.info("We are dividing 1 by 0")
        x = 1/0
    except Exception as e:
        raise SensorException(e, sys) # type: ignore


if __name__ == "__main__":
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
    mongodb_client = MongoDBClient()
    print("Collection names:", mongodb_client.database.list_collection_names())
