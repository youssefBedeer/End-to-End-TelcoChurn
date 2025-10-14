import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s")



list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # create dirs
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    # create files 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass 
    
        
    else:
        logging.info(f"{filename} already exist.")
        
    