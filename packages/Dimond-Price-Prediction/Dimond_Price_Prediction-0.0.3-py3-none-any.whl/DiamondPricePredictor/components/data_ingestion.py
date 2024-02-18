import os
import urllib.request as request
import zipfile
from pathlib import Path
from DiamondPricePredictor.logger import logging
from DiamondPricePredictor.utils.common import get_size
from DiamondPricePredictor.entity.config_entity import DataIngestionConfig

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        api=KaggleApi()
        api.authenticate()

    
    def download_train_file(self):
        if not os.path.exists(self.config.local_data_file_train):
            api=KaggleApi()
            api.authenticate()
            api.competition_download_file('playground-series-s3e8',file_name='train.csv',path=self.config.root_dir)
            logging.info("Train file download completed:")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file_train))}")  

    def download_test_file(self):
        if not os.path.exists(self.config.local_data_file_test):
            api=KaggleApi()
            api.authenticate()
            api.competition_download_file('playground-series-s3e8',file_name='test.csv',path=self.config.root_dir)
            logging.info("Test File Download completed")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file_test))}")  
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file_train, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logging.info("Train file extraction completed")
        with zipfile.ZipFile(self.config.local_data_file_test, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logging.info("Test file extraction completed")