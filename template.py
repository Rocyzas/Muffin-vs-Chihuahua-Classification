import os
from pathlib import Path
import logging

logging.basicConfig(filename='TemplateCreation.log', filemode='a', level=logging.WARNING)

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:

    filedir, filename = os.path.split(file)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename}")
    
    if(not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file, 'w') as f:
            pass
            logging.info(f"Creating empty file {file}")
        
    else:
        logging.warning(f"{file} already exist")