import os
import yaml
from src.DSPROJECT import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        ValueError: If the yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): List of directories
        verbose (bool, optional): Whether to log the directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")    


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a json file

    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object

    Args:
        path (Path): Path to the json file

    Raises:
        e: empty file

    Returns:
        ConfigBox: ConfigBox object
    """
    
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Data loaded from the binary file

    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
    