import os 
import yaml 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from src import logging, CustomException
import json
from typing import Any 
import joblib

@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    try:
        with open(yaml_path, "r") as f:
            content = yaml.safe_load(f)
            logging.info(f"reading the content of '{yaml_path}'")
            return ConfigBox(content)

    except Exception as e:
        raise CustomException(e) from e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save a dictionary as a JSON file."""
    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"JSON file saved at: {path}")
    
    
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(data, path)
    logging.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


# import os 
# import sys
# import pandas as pd 
# import numpy as np 
# import dill
# import pickle
# from sklearn.metrics import r2_score
# from sklearn.model_selection import GridSearchCV

# def save_object(file_path, obj):
#     try:
#         dir_path = os.path.dirname(file_path)
#         os.makedirs(dir_path, exist_ok=True)
#         with open(file_path, "wb") as file_obj:
#             pickle.dump(obj, file_obj)
#     except Exception as e: 
#         EC = CustomException(e,sys)
#         logging.error(EC)
#         raise EC
    
# def load_object(file_path:str):
#     try:
#         with open(file_path, "rb") as  file_obj:
#             return dill.load(file_obj)

#     except Exception as e: 
#         raise CustomException(e)
    
# def evaluate_model(X_train, X_test, y_train, y_test, models, params):
#     try:
#         report = {} 

#         for i in range(len(list(models))):
#             model_name = list(models.keys())[i]
#             model = list(models.values())[i]
#             param = params[list(params.keys())[i]]

#             # hyperparameter tunning
#             gs = GridSearchCV(estimator=model, param_grid=param, cv=3)
#             gs.fit(X_train, y_train)

#             best_model = gs.best_estimator_
#             best_model.fit(X_train,y_train)

#             y_train_pred = best_model.predict(X_train)
#             y_test_pred = best_model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_pred)
#             test_model_score = r2_score(y_test, y_test_pred)
#             logging.info(f"best params for {model_name}: {gs.best_params_} with score: '{test_model_score}'")

#             report[model_name] = {
#                 "score":test_model_score,
#                 "model": best_model,
#                 "params": gs.best_params_
                
#             }

#         return report


#     except Exception as e: 
#         EC = CustomException(e,sys)
#         logging.error(EC)
#         raise EC
    



