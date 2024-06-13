import csv
import json
import sys

def tsv_to_json(tsv_file, json_file):
    with open(tsv_file, mode='r') as tsv_f:
        reader = csv.DictReader(tsv_f, delimiter='\t')
        data = [row for row in reader]

    with open(json_file, mode='w') as json_f:
        json.dump(data, json_f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tsv_to_json.py <input_tsv_file> <output_json_file>")
        sys.exit(1)

    input_tsv_file = sys.argv[1]
    output_json_file = sys.argv[2]

    tsv_to_json(input_tsv_file, output_json_file)
