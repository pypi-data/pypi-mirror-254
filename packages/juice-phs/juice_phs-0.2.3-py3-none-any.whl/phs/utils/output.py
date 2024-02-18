import csv
from itertools import zip_longest

from .setup import get_version_from_setup_cfg
VERSION = get_version_from_setup_cfg()


def write_csv(header_list, data_columns, file_name, title, resolution):
    # Check if the length of header_list matches the number of data columns
    if len(header_list) != len(data_columns):
        raise ValueError("Number of columns in header doesn't match number of data columns")

    data_rows = list(zip_longest(*data_columns))  # Transpose the data columns to rows

    with open(file_name, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        # Write the header
        csvfile.write(f'# {title}\n')
        csvfile.write(f'# Generation date: {title}\n')
        csvfile.write(f'# JUICE-SHT version: {VERSION}\n')
        csvfile.write(f'# Resolution (sec): {resolution:.0f}\n')
        csvfile.write(f'# {",".join(map(str, header_list))}\n')
        # Write the data rows
        writer.writerows(data_rows)

    return