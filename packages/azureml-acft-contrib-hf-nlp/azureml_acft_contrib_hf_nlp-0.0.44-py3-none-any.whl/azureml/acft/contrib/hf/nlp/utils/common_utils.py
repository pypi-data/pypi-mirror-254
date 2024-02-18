# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""
common utils
"""

import json
import os
from typing import Dict, Any, TypeVar
from copy import deepcopy
from pathlib import Path

import torch

import logging

from azureml.acft.common_components import get_logger_app, set_logging_parameters, LoggingLiterals
from azureml.acft.common_components.utils.error_handling.exceptions import ACFTValidationException
from azureml.acft.common_components.utils.error_handling.error_definitions import ACFTUserError
from azureml.acft.common_components.utils.run_utils import post_warning
from azureml._common._error_definition.azureml_error import AzureMLError
from azureml.core.run import Run

logger = get_logger_app(__name__)

KeyType = TypeVar('KeyType')
TRAIN_FILE_NAME = "train_input.jsonl"
VALIDATION_FILE_NAME = "validation_input.jsonl"


def deep_update(src_mapping: Dict[KeyType, Any], *updating_mappings: Dict[KeyType, Any]) -> Dict[KeyType, Any]:
    updated_mapping = src_mapping.copy()
    for updating_mapping in updating_mappings:
        for k, v in updating_mapping.items():
            if k in updated_mapping and isinstance(updated_mapping[k], dict) and isinstance(v, dict):
                updated_mapping[k] = deep_update(updated_mapping[k], v)
            else:
                updated_mapping[k] = v
    return updated_mapping


def dict_to_json_serializable(d: Dict[str, Any]) -> None:
    """
    Convert the passed dictionary to JSON serializable format by removing unsupported data types as values
    so that the dictionary can be saved as json file
    """
    UNSUPPORTED_JSON_DATA_FORMATS = [
        torch.dtype,
        Path,
    ]

    for key in list(d.keys()):
        if any([isinstance(d[key], data_format) for data_format in UNSUPPORTED_JSON_DATA_FORMATS]):
            d.pop(key)

    # do the same for nested dictionary
    for value in d.values():
        if isinstance(value, dict):
            dict_to_json_serializable(value)


def write_dict_to_json_file(d: Dict[str, Any], file_name: str) -> None:
    """
    Convert the passed dictionary to JSON serializable and write to json file
    """
    Path(file_name).parent.mkdir(exist_ok=True, parents=True)
    
    json_dict = deepcopy(d)
    # convert dictionary to JSON serializable
    dict_to_json_serializable(json_dict)
    # write dictionary to json file
    with open(file_name, 'w') as rptr:
        json.dump(json_dict, rptr, indent=2)


def filter_invalid_data_rows_for_jsonl(file_path: str,
                                       destination_folder_path: str,
                                       mode: str = "train"):
    """Processes a file, appends its lines to destination_file, returns # lines."""

    if not os.path.exists(file_path):
        raise ACFTValidationException._with_error(
                AzureMLError.create(
                    ACFTUserError,
                    pii_safe_message=(
                        f"The provided file does not exist: {file_path}"
                    )
                )
            )

    if mode == "train":
        destination_file_path = (Path(destination_folder_path) / TRAIN_FILE_NAME).resolve()
    else:
        destination_file_path = (Path(destination_folder_path) / VALIDATION_FILE_NAME).resolve()

    if os.path.exists(destination_file_path):
        os.remove(destination_file_path)
        logging.info("Output file already exists, wipe it before writing data into it.")

    # Read the file using UTF-8-sig encoding to remove BOM
    invalid_json_ct = 0
    with open(file_path, "rt", encoding="UTF-8-sig") as f_in, \
         open(destination_file_path, "a", encoding="UTF-8") as f_out:

        for index, line in enumerate(f_in):
            # Check for empty lines in dataset rows
            if not line.strip():
                msg = f"Line number {index} is empty. Skipping"
                invalid_json_ct += 1
                logging.warning(msg)
                continue

            # Check if the line is a valid json
            try:
                logging.info(f"Loading file {file_path}")
                example = json.loads(line)
            except Exception as e:
                # logging.info(f"Failed to load file {file_path}")
                error_type = type(e).__name__
                error_msg = str(e)
                logging.warning(f"Bad input data {file_path} on line {index}. {error_type}: {error_msg}, skipping..")
                invalid_json_ct += 1
                continue

            f_out.write(json.dumps(example))
            f_out.write("\n")

    # Post warning to Run level about number of lines skipped
    if invalid_json_ct > 0:
        warning_message = (f"Total {invalid_json_ct} json lines skipped in your dataset," +
                           "due to either empty or invalid format of json.")
        logging.warning(warning_message)
        try:
            run = Run.get_context()
            top_level_run = run
            while top_level_run.parent:
                top_level_run = top_level_run.parent
            post_warning(top_level_run, warning_message)
        except Exception as e:
            logging.warning(f"Post warning to parent pipeline run failed with exception {e}")
