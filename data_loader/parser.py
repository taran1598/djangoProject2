import csv

import pandas
from data_loader.models import FoodName, NutrientName, NutrientAmount


class ParserCSV:

    def populate_model_from_csv_file(self, src_file_to_parse, model_to_populate):
        """
        Reads csv file from self.src_file_to_parse and populates the specified model
        :return: Returns iterator, where each iteration returns row of csv file
        """
        with open(src_file_to_parse, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                model_to_populate(row)

    def populate_model_from_csv_file_pandas(self, src_file_to_parse, model_to_populate, encoding='utf-8'):
        """
        Reads csv file from self.src_file_to_parse and populates the specified model
        :return: Returns iterator, where each iteration returns row of csv file
        """
        df = pandas.read_csv(src_file_to_parse, encoding=encoding)
        model_to_populate(df)

