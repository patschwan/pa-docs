import csv
import os
from dotenv import load_dotenv

load_dotenv(override=True)
path_to = os.getenv('EXPORT_PATH')

def exp_c_list(filename: str, to_csv: list):
    """Export List of Cubes to CSV
        Arguments:
            filename: str
            to_csv: list of dicts
    """
    if not to_csv:
        return

    # Get the headers from the keys of the first dictionary
    headers = to_csv[0].keys()

    with open(path_to + filename + ".csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')

        writer.writeheader()
        for row in to_csv:
            writer.writerow(row)

