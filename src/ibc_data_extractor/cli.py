import argparse


def command_line_parser():
    parser = argparse.ArgumentParser(description="IBC Chain Data Extractor")
    parser.add_argument('-o', '--output', type=str, nargs='+', required=True, choices=['screen', 'csv', 'excel'],
                        help="Specify one or more output types: 'screen', 'csv', 'excel'. Can specify multiple by separating with spaces.")
    parser.add_argument('-u', '--url', type=str, default='https://github.com/cosmos/chain-registry',
                        help="Optional: Specify the GitHub repository URL. Defaults to the Cosmos Chain Registry.")
    parser.add_argument('-n', '--name', type=str,
                        help="Optional: Specify a base name for the output file(s). If omitted, defaults to 'ibc_data_TIMESTAMP'.")
    return parser.parse_args()