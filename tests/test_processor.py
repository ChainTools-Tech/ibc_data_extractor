# test_processor.py
from src.ibc_data_extractor import process_files
from zipfile import ZipFile
from io import BytesIO


def test_process_files():
    # Mocking a simple JSON data as if it were read from a zipfile
    mock_zip_file_content = b'{"chain_1": {"chain_name": "mockchain1", "client_id": "client123", "connection_id": "conn456"}, "chain_2": {"chain_name": "mockchain2", "client_id": "client789", "connection_id": "conn012"}}'
    mock_zip_info = ZipFile(BytesIO(), mode='w')
    mock_zip_info.writestr('mock_data.json', mock_zip_file_content)

    processed_data = process_files(mock_zip_info)
    assert processed_data is not None
    assert type(processed_data) is list
    assert len(processed_data) > 0

    mock_zip_info.close()
