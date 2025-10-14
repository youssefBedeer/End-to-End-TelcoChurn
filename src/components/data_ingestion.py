from urllib.request import urlretrieve
from src import logging, CustomException
import zipfile
import rarfile
import os
from src.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                file_name, headers = urlretrieve(
                    url= self.config.source_url, 
                    filename=self.config.local_data_file
                )
                logging.info(f"{file_name} download!")
            else:
                logging.info(f"{self.config.local_data_file} already exist.")
        except Exception as e:
            raise CustomException(e) from e
            
    

    def extract_file(self):
        try:
            local_file = self.config.local_data_file
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            
            # check if there is csv file 
            if any(f.endswith(".csv") for f in os.listdir(self.config.root_dir)):
                logging.info("csv file exist")
            elif zipfile.is_zipfile(local_file):
                with zipfile.ZipFile(local_file, "r") as f:
                    f.extractall(unzip_dir)
                logging.info("ZIP file extracted successfully.")

            elif rarfile.is_rarfile(local_file):
                with rarfile.RarFile(local_file, "r") as f:
                    f.extractall(unzip_dir)
                logging.info("RAR file extracted successfully.")

            else:
                raise CustomException(f"Unsupported or corrupt file format: {local_file}")

        except Exception as e:
            raise CustomException(e) from e
