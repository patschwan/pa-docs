import csv
import os

from dotenv import load_dotenv

load_dotenv(override=True)
exp_path = os.getenv("EXPORT_PATH")

# Example usage:
# exp_c_list("test_export", [{'name': 'cube1', 'dimension': 'dim1'}])


def exp_c_list(filename: str, to_csv: list):
    """Export List of Cubes to CSV
    Arguments:
        filename: str
        to_csv: list of dicts
    """
    # Validate inputs
    if not to_csv:
        print("Warning: Empty list provided for export")
        return

    if not isinstance(to_csv, list):
        print("Error: to_csv must be a list")
        return

    if not exp_path:
        print("Error: EXPORT_PATH environment variable is not set")
        return

    # Ensure export directory exists
    try:
        os.makedirs(exp_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating export directory: {e}")
        return

    # Validate that to_csv contains dictionaries
    if not all(isinstance(item, dict) for item in to_csv):
        print("Error: All items in to_csv must be dictionaries")
        return

    # Get headers from the first dictionary (or create empty headers if needed)
    try:
        headers = list(to_csv[0].keys()) if to_csv else []
    except Exception as e:
        print(f"Error getting headers from data: {e}")
        return

    # Create full file path with proper separators
    file_path = os.path.join(exp_path, filename + ".csv")

    try:
        with open(
            file_path + filename + ".csv", "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")

            writer.writeheader()
            for row in to_csv:
                # Ensure each row has all required fields
                if isinstance(row, dict):
                    writer.writerow(row)
                else:
                    print(f"Warning: Skipping non-dictionary row: {row}")

    except Exception as e:
        print(f"Error writing CSV file: {e}")
        return
