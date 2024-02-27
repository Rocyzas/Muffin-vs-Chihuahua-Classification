from PIL import Image
import os
from cnnClassifier.entity.config_entity import DataPreparationConfig

class DataPreparation:
    def __init__(self, config: DataPreparationConfig):
        self.config = config

    def convert_to_224x224_chihuahua_files(self):
        self._resize_images_in_directory(self.config.local_data_file_c)

    def convert_to_224x224_muffin_files(self):
        self._resize_images_in_directory(self.config.local_data_file_m)

    def _resize_images_in_directory(self, directory):
        for filename in os.listdir(directory):
            if filename.startswith('.'):
                filepath = os.path.join(directory, filename)
                os.remove(filepath)
            elif filename.endswith(".jpg"):
                filepath = os.path.join(directory, filename)
                img = Image.open(filepath)
                img = img.resize((224, 224))
                img.save(filepath)
