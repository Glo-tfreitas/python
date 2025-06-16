import csv
from pathlib import Path

datafile = 'data.csv'
cfgFileDirectory = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(datafile)

def get_data():
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader) # We skip the first row.
        data = [tuple(row) for row in reader]
    return data

print(get_data())