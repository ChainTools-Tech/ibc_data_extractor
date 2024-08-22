## Overview  
  
This Python script downloads and parse IBC JSON files from a chain-registry GitHub repository. 
It extracts detailed information about blockchain interconnectivity and allows for various output options including on-screen display, CSV, and Excel files.  
  
## Features  
  
- **Configurable Download Source**: Fetches data from any specified GitHub repository  (default: https://github.com/cosmos/chain-registry).
- **Multiple Output Formats**: Outputs the data on-screen or exports it to CSV or Excel files.  
- **Customizable Output Filenames**: Allows specifying custom filenames for output files, or uses a timestamped filename by default.  
  
## Requirements  
  
- Python 3.6 or newer  
- Pandas Library  
- Requests Library 
- Openpyxl Library 
  
## Installation

Clone source repository.
```bash
git clone https://github.com/ChainTools-Tech/ibc_data_extractor.git
cd ibc_data_extractor
```

Create virtual environment and install package.
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install .
```

## Usage  
  
The script is executed from the command line, and users can specify several options for output and configuration:  
  
### Command Line Arguments  
  
- **Output Type** (`-o`, `--output`):  
  - Specify one or more output types: 'screen', 'csv', 'excel'.  
  - Multiple output types can be specified by separating them with spaces.  
- **Repository URL** (`-u`, `--url`):  
  - Optionally specify the GitHub repository URL to download data from.  
  - If not specified, it defaults to the Cosmos Chain Registry.  
- **Output Filename** (`-n`, `--name`):  
  - Optionally specify a base name for the output file(s).  
  - If omitted, the filename defaults to 'ibc_data_TIMESTAMP', where TIMESTAMP is the current timestamp.  
  
### Examples  
  
- **Display data on-screen**:  
```bash  
ibc_data_extractor --output screen  
```  
- **Save data to CSV and Excel files with a custom filename**:  
```bash
ibc_data_extractor --output csv excel --name custom_filename  
```  
- **Use a custom repository URL and save to a timestamp-named CSV file**:  
```bash  
ibc_data_extractor --output csv --url https://github.com/another-repository
```  
## Output  
  
The script generates tabular data with the following columns:  
  
- `chain_1_chain_name`  
- `chain_1_client_id`  
- `chain_1_connection_id`  
- `chain_1_channel_id`  
- `chain_2_chain_name`  
- `chain_2_client_id`  
- `chain_2_connection_id`  
- `chain_2_channel_id`  
  
Each row in the output files or on-screen display represents data extracted from a single JSON file found in the `_IBC` directory of the specified GitHub repository.  
  
## Logging  
  
Detailed logging provides insights into the script’s operations, aiding in debugging and verification of the process.  
  
## Customization and Extension  
  
The script can be easily modified to accommodate additional data fields, interface with different JSON structures, or integrate with other data processing workflows.  
  
## Support  
  
For any issues or questions, please open an issue in the GitHub repository where this script is hosted, or contact the maintainer directly.

## Packaging and Distribution

### Building the Package

To package the IBC Data Extractor for distribution:

1. Ensure you have the required packages to build the distribution:

```bash
pip install build
```

2. From the root directory of the project, run:

```bash
python -m build
```

This command generates distribution files in the `dist/` directory.


## License

This project is licensed under the MIT License - see the LICENSE file for details.