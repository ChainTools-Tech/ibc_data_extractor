import json
import logging
from ibc_data_extractor.config import BRANCH, REPO_SUBDIR

def process_files(zipfile):
    files = [f for f in zipfile.namelist() if f.startswith(f"chain-registry-{BRANCH}/{REPO_SUBDIR}/") and f.endswith('.json')]
    logging.info(f"Found {len(files)} JSON files in the specified directory.")
    data = []

    for file_path in files:
        logging.info(f"Processing file: {file_path}")
        with zipfile.open(file_path) as file:
            json_data = json.load(file)
            channel_data = json_data["channels"][0] if json_data["channels"] else {}
            entry = {
                "chain_1_chain_name": json_data["chain_1"].get("chain_name"),
                "chain_1_client_id": json_data["chain_1"].get("client_id"),
                "chain_1_connection_id": json_data["chain_1"].get("connection_id"),
                "chain_1_channel_id": channel_data.get("chain_1", {}).get("channel_id"),
                "chain_2_chain_name": json_data["chain_2"].get("chain_name"),
                "chain_2_client_id": json_data["chain_2"].get("client_id"),
                "chain_2_connection_id": json_data["chain_2"].get("connection_id"),
                "chain_2_channel_id": channel_data.get("chain_2", {}).get("channel_id")
            }
            data.append(entry)
    return data