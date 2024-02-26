import os
import zipfile
import shutil
from urllib import request
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_chichuahua_files(self):

        for i in range(1, self.config.num_chihuahua_files + 1):
            file_url = f"{self.config.source_URL}/c{i}.zip"
            local_file = os.path.join(self.config.root_dir, f"data_c/c{i}.zip")
            if not os.path.exists(local_file):
                os.makedirs(os.path.dirname(local_file), exist_ok=True)
                filename, headers = request.urlretrieve(
                    url=file_url, 
                    filename=local_file
                    )
                logger.info(f"{filename} downloaded with the following info:\n{headers}")
            else:
                logger.info(f"File already exists at {local_file}")
    
    def download_muffin_files(self):

        for i in range(1, self.config.num_muffin_files + 1):
            file_url = f"{self.config.source_URL}/m{i}.zip"
            local_file = os.path.join(self.config.root_dir, f"data_m/m{i}.zip")
            if not os.path.exists(local_file):
                os.makedirs(os.path.dirname(local_file), exist_ok=True)
                filename, headers = request.urlretrieve(
                    url=file_url, 
                    filename=local_file
                    )
                logger.info(f"{filename} downloaded with the following info:\n{headers}")
            else:
                logger.info(f"File already exists at {local_file}") 


    def extract_chihuahua_files(self):
        unzip_dir = os.path.join(self.config.unzip_dir, 'c')
        os.makedirs(unzip_dir, exist_ok=True)
        
        for i in range(1, self.config.num_chihuahua_files + 1):
            local_zip_file = os.path.join(self.config.root_dir, f"data_c/c{i}.zip")
            with zipfile.ZipFile(local_zip_file, 'r') as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.basename(member)
                    if not filename:
                        continue
                    source = zip_file.open(member)
                    target_path = os.path.join(self.config.unzip_dir, 'c', filename)
                    with source, open(target_path, "wb") as target:
                        shutil.copyfileobj(source, target)

    def extract_muffin_files(self):
        unzip_dir = os.path.join(self.config.unzip_dir, 'm')
        os.makedirs(unzip_dir, exist_ok=True)
        
        for i in range(1, self.config.num_muffin_files + 1):
            local_zip_file = os.path.join(self.config.root_dir, f"data_m/m{i}.zip")
            with zipfile.ZipFile(local_zip_file, 'r') as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.basename(member)
                    if not filename:
                        continue
                    source = zip_file.open(member)
                    target_path = os.path.join(self.config.unzip_dir, 'm', filename)
                    with source, open(target_path, "wb") as target:
                        shutil.copyfileobj(source, target)
    
    def cleanup_zips(self):
        try:
            shutil.rmtree(os.path.join(self.config.root_dir, "data_c"))
        except FileNotFoundError:
            pass

        try:
            shutil.rmtree(os.path.join(self.config.root_dir, "data_m"))
        except FileNotFoundError:
            pass

        try:
            shutil.rmtree(os.path.join(self.config.root_dir, 'c/__MACOSX'))
        except FileNotFoundError:
            pass

        try:
            shutil.rmtree(os.path.join(self.config.root_dir, 'm/__MACOSX'))
        except FileNotFoundError:
            pass
