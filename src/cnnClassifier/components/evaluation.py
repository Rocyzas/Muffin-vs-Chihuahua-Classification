import os 
import tensorflow as tf
from dataclasses import dataclass
from pathlib import Path

from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories, save_json

from urllib.parse import urlparse
