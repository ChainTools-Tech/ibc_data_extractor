import requests
import logging
from io import BytesIO
from zipfile import ZipFile
from ibc_data_extractor.config import BRANCH

def download_data(url):
    archive_url = f"{url}/archive/{BRANCH}.zip"
    logging.info(f"Downloading the repository zip archive from {archive_url}...")
    response = requests.get(archive_url)

    if response.status_code == 200:
        logging.info("Download successful. Processing the zip file...")
        return ZipFile(BytesIO(response.content))
    else:
        logging.error(f"Failed to download the repository. Status code: {response.status_code}")
        exit(1)