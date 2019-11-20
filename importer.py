import os
import json
from abc import ABCMeta, abstractmethod
from dicttoxml import dicttoxml
from collections import namedtuple
from exceptions import InvalidDict
from utils import is_url, is_within_range, max_length
from enums import OutPutEnum, FileType
ProcessedFile = namedtuple('ProcessedFile', ['output_file_name', 'is_temporary'])
import sys
validations = {
    "name": lambda x: isinstance(x, str) and max_length(x, 100),
    "address": lambda x: len(x) > 0,
    "stars": lambda x: is_within_range(x, 0, 5),
    "contact": lambda x: len(x) > 0,
    "phone": lambda x: len(x) > 0,
    "url": lambda x: is_url(x),
}


class RowBasedImporter(object):
    __metaclass__ = ABCMeta

    received_data = []
    output_format = OutPutEnum.JSON
    type = FileType.CSV

    def __init__(self, filepath='', type=None, output_format=None):
        if not os.path.exists(filepath):
            raise FileExistsError
        if output_format is not None:
            try:
                self.output_format = OutPutEnum[output_format.upper()]
            except KeyError:
                print("Invalid output options added, Please use json or xml")
                sys.exit()
        if type is not None:
            try:
                self.type  = FileType[type.upper()]
            except KeyError:
                print("Invalid type options added, Please use CSV for now ")
                sys.exit()
    @property
    @abstractmethod
    def skip_header(self):
        """ Denotes whether to skip the header line of the row-based file
        """
        pass

    @property
    @abstractmethod
    def key_names(self):
        """ Array of strings corresponding to the columns to be used as the
            compound primary key
        """
        pass

    @property
    @abstractmethod
    def data_settings(self):
        """ The settings hash to use to connect to the right integration
        """
        pass

    @abstractmethod
    def parse_row(self, row):
        """ Parse a row into the row data to be inserted into Redshift
        """
        pass

    def preprocess_file(self, filename):
        """ Pre-process the row-based file, if necessary.  The default implementation
            returns (filename, False).

        :param filename the filename of the original file
        :return tuple containing the (possibly) new filename
                of the processed file and a boolean value denoting
                whether the pre-processed file should be deleted
        """
        return ProcessedFile(output_file_name=filename, is_temporary=False)

    def get_present_column_count(self, row):
        return len([col for col in row if col])

    def is_empty_row(self, row):
        return self.get_present_column_count(row) == 0

    @abstractmethod
    def get_rows(self, filename):
        """
        Return the rows in the specified filename.  The returned value must only
        be iterable. i.e. it can be a generator or a list

        :param filename: the filename containing the rows
        :return: the rows in the specified filename
        """
        pass

    def is_valid_data(self):
        """
        Valids dict data obtained from csv or other input medium
        :return boolean True if dictionary is valid:
        """
        """if not isinstance(self.received_data, dict):
            print(self.received_data)"""

        for data in self.received_data:
            if not all(validations.get(k, lambda x: False)(v) for k, v in data.items()):
                return False
        return True

    def output_data(self):
        """
        converts data uploaded to the expected out
        :return:
        """
        if not self.is_valid_data():
            raise InvalidDict

        if self.output_format is OutPutEnum.XML:
           self.received_data = self.xml_output()
        elif self.output_format is OutPutEnum.JSON:
            self.received_data = self.json_output()

        return self.received_data

    def xml_output(self):
        """
        converts dict to xml
        :return xml:
        """
        return dicttoxml(self.received_data, custom_root='data', attr_type=False)

    def json_output(self):
        """
        coverts dict to json
        :return json:
        """
        return  json.dumps(self.received_data)