import sys
import csv
import argparse

from importer import RowBasedImporter
from exceptions import FailedToGetData

class CSVImporter(RowBasedImporter):

    """def __init__(self, delimiter=',', arguments=sys.argv[1:]):
        RowBasedImporter.__init__(self)
        delimiter_from_arguments = self._parse_delimiter_from_arguments(arguments)

        self._delimiter = delimiter_from_arguments or delimiter"""

    _delimiter = ','

    def _parse_delimiter_from_arguments(self, arguments):
        parser = argparse.ArgumentParser()
        parser.add_argument('--csv-importer-delimiter',
                            type=str,
                            help='The delimiter of the CSV file')
        args, _ = parser.parse_known_args(args=arguments)
        delimiter = args.csv_importer_delimiter.decode('string_escape') if args.csv_importer_delimiter else None
        return delimiter

    @property
    def delimiter(self):
        return self._delimiter

    def get_rows(self, filename):
        try:
            with open(filename, "rU") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=self.delimiter)
                for row in reader:
                    yield row
                #self.received_data = [dict(d) for d in reader]
        except FailedToGetData:
            pass