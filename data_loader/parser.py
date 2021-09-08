import csv

import pandas
from data_loader.models import FoodName, NutrientName, NutrientAmount, MeasureName, ConversionFactor


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

    def populate_model_from_csv_file_pandas(self, src_file_to_parse, encoding='iso-8859-1'):
        """
        Reads csv file from self.src_file_to_parse and populates the specified model
        :return: Returns iterator, where each iteration returns row of csv file
        """
        return pandas.read_csv(src_file_to_parse, encoding=encoding)

    @staticmethod
    def populateDatabase(file_dict):
        """
        Populates database from the csv files in file_dict
        :param file_dict: dictionary containing
        :return:
        """

        parser = ParserCSV()

        try:

            # make sure the file pointer is at the start. Otherwise we won't read any
            file_dict['food_name_file_name'].file.seek(0)
            file_dict['nutrient_name_file_name'].file.seek(0)
            file_dict['nutrient_amount_file_name'].file.seek(0)
            file_dict['measure_name_file_name'].file.seek(0)
            file_dict['conversion_factor_file_name'].file.seek(0)

            FoodName.populate_model_food_name_dataframe(
                parser.populate_model_from_csv_file_pandas(file_dict['food_name_file_name'].file))

            NutrientName.populate_model_nutrient_name_dataframe(
                parser.populate_model_from_csv_file_pandas(file_dict['nutrient_name_file_name'].file))

            NutrientAmount.populate_model_nutrient_amount_dataframe(
                parser.populate_model_from_csv_file_pandas(file_dict['nutrient_amount_file_name'].file))

            MeasureName.populate_model_measure_name_dataframe(
                parser.populate_model_from_csv_file_pandas(file_dict['measure_name_file_name'].file))

            ConversionFactor.populate_model_conversion_factor_dataframe(
                parser.populate_model_from_csv_file_pandas(file_dict['conversion_factor_file_name'].file))

        except KeyError:
            raise KeyError("File is missing")