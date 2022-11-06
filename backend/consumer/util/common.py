import json
import os
import logging
import re
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_timestamp_from_filename(file_path: str):
    match = re.search(r"(\d+)", file_path)
    ts = datetime.strptime(match.group(1), '%Y%m%d%H%M')
    return ts


def check_file_is_outdated(file_path: str, delay_in_sec: int) -> bool:
    is_available = os.path.exists(file_path)
    if not is_available:
        logger.info(f"file is not available in {file_path}")
        return True
    else:
        most_recent_version = get_timestamp_from_filename(file_path)
        if (datetime.now() - most_recent_version).total_seconds() < delay_in_sec:
            return False
        else:
            return True


def save_json(file_path: str, file) -> bool:
    try:
        logger.debug(f'file exists in {file_path}: {os.path.exists(file_path)}')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(file, f)
        return True
    except Exception as e:
        logger.warning(f'Could not save file due to: {e}')
        return False


def open_json(file_path: str) -> dict:
    try:
        logger.debug(f'file exists in {file_path}: {os.path.exists(file_path)}')
        with open(file_path, 'r') as file:
            json_dict = json.load(file)
        return json_dict
    except Exception as e:
        logger.error(f'Could not open file due to: {e}')
        return {}