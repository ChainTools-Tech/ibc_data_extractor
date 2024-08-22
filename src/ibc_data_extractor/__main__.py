from ibc_data_extractor.cli import command_line_parser
from ibc_data_extractor.downloader import download_data
from ibc_data_extractor.processor import process_files
from ibc_data_extractor.outputter import output_data
from ibc_data_extractor.logger import initialize_logger


def main():
    cmdargs = command_line_parser()
    initialize_logger()

    zipfile = download_data(cmdargs.url)
    data = process_files(zipfile)
    output_data(data, cmdargs.output, cmdargs.name)

if __name__ == "__main__":
    main()