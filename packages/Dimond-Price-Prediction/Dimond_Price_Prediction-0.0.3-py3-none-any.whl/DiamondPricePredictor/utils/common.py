import os
import sys
from box.exceptions import BoxValueError
import yaml
import json
import dill
import joblib
from DiamondPricePredictor.logger import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
from pathlib import Path
from DiamondPricePredictor.exception import CustomException

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    path = Path(path)
    print(path)
    with open(path,"w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")

@ensure_annotations
def save_loaded_json(path: str, data: ConfigBox):
    """save json data

    Args:
        path (str): path to json file
        data (configbox): data to be saved in json file
    """
    path = Path(path)
    print(path)
    with path.open("w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
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


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

def save_obj(file_path,obj):
    try:
        dire_path=os.path.dirname(file_path)
        os.makedirs(dire_path,exist_ok=True)
        with open(file_path,"wb") as file_Obj:
            joblib.dump(obj,file_Obj)

    except Exception as e:
        raise CustomException(sys,e)

if __name__ == "__main__":
    logging.info("Logger is set for common.py file")