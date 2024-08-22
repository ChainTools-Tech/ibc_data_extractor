import pandas as pd
import logging
from datetime import datetime


def output_data(data, output_types, filename=None):
    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename = filename if filename else f"ibc_data_{timestamp}"

    if 'csv' in output_types:
        csv_filename = f"{base_filename}.csv"
        df.to_csv(csv_filename, index=False)
        logging.info(f"Data saved to {csv_filename}.")
    if 'excel' in output_types:
        excel_filename = f"{base_filename}.xlsx"
        df.to_excel(excel_filename, index=False)
        logging.info(f"Data saved to {excel_filename}.")
    if 'screen' in output_types:
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(df)