import os
import json
from datetime import datetime

import click as click
import requests
import logging

from util.common import check_file_is_outdated, save_json, open_json
from manipulator.filter_league_data import filter_dict, clean_seasons

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_data(url, headers, payload):
    logger.info(f'send request to {url}')
    response = requests.request("GET", url, headers=headers, data=payload)
    raw_data = json.loads(response.text)
    return raw_data


mapper = {
    "": "",
    "all_teams": "teams",
    "all_leagues": "leagues",
    "all_venues": "venues",
}


def _get_data_from(endpoint: str, headers: dict, payload: dict):
    deprecated = 24*60*60
    endpoint = f"{endpoint}"
    url = f"https://v3.football.api-sports.io/{mapper[endpoint]}"
    ts_version = datetime.now().strftime('%Y%m%d%H%M')
    storage_path = f"data/raw_{endpoint}_{ts_version}.json"
    logger.info(f'Try to fetch data from {url}')
    if check_file_is_outdated(storage_path, 24*60*60):
        data = download_data(url=url, headers=headers, payload=payload)
        if save_json(file_path=storage_path, file=data):
            logger.info(f'File saved to {storage_path}')
    else:
        logger.info(f'File {storage_path} already exists and was updated less than {deprecated} seconds.')


@click.group("cli")
@click.pass_context
def cli(ctx):
    """An example CLI for interfacing with a document"""
    ctx.obj = "some context here"


@cli.command("get-data")
@click.pass_context
@click.option("--endpoint", help="endpoint to query (leagues,...)", type=str)
def get_data(ctx, endpoint: str):
    endpoints = [k for k, v in mapper.items()]
    apikey = os.environ.get('FOOTBALL_COM_API')
    payload = {}
    headers = {
        'x-rapidapi-key': f'{apikey}',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    if endpoint in endpoints:
        _get_data_from(endpoint=endpoint, headers=headers, payload=payload)
    else:
        logger.info(f'Not implemented yet: "{endpoint}". Choose one of the following: {endpoints}')


if __name__ == '__main__':
    cli()