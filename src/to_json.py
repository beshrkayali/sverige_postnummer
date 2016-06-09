# -*- coding: utf-8 -*-
from collections import defaultdict
from csv import DictReader
import json
import io


class CsvToJson(object):
    def __init__(self, csv_file, json_output, aggregate_key):
        self.csv_file = csv_file
        self.json_output = json_output
        self.aggregate_key = aggregate_key

    def read_csv(self):
        output = defaultdict(list)
        with open(self.csv_file, 'r') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                c = row.pop(self.aggregate_key)
                output[c].append(row)

        return output

    def to_json(self):
        data = self.read_csv()

        with io.open(self.json_output, 'w', encoding='utf-8') as jsonfile:
            d = json.dumps(data, ensure_ascii=False).decode("utf-8")
            jsonfile.write(d)

if __name__ == '__main__':
    ctj = CsvToJson(
        csv_file='../postcodes.csv',
        json_output='../postcodes.json',
        aggregate_key='Code'
    )

    ctj.to_json()
