import csv
import math

import pandas
from website_name.models import FoodName, NutrientName, NutrientAmount


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

    def populate_model_from_csv_file_pandas(self, src_file_to_parse, model_to_populate):
        """
        Reads csv file from self.src_file_to_parse and populates the specified model
        :return: Returns iterator, where each iteration returns row of csv file
        """
        df = pandas.read_csv(src_file_to_parse)
        model_to_populate(df)
        # df.to_sql(FoodName, con=settings.DATABASES.get('ENGINE'))
        # batch_food_name_objects = [
        #     FoodName(
        #         food_id=row['FoodID'],
        #         food_code=row['FoodCode'],
        #         food_group_id=row['FoodGroupID'],
        #         food_source_id=row['FoodSourceID'],
        #         food_desc=row['FoodDescription'],
        #         food_desc_f=row['FoodDescriptionF'],
        #         food_date_of_entry=row['FoodDateOfEntry'],
        #         food_date_of_publication="" if math.isnan(row['FoodDateOfPublication']) else row['FoodDateOfPublication'],
        #         country_code=-1 if math.isnan(row['CountryCode']) else row['CountryCode'],
        #         scientific_name="" if math.isnan(row['ScientificName']) else row['ScientificName']
        #     )
        #     for i, row in df.iterrows()
        # ]
        # FoodName.objects.bulk_create(batch_food_name_objects)

    @staticmethod
    def string_to_list(string_to_convert, delimiter) -> list:
        """
        Converts string to list. Splits string on the delimiter
        :param string_to_convert: string to convert to a list
        :param delimiter: the delimiter that decides where to split the list
        :return: list that is the result of splitting the list on the delimiter
        """
        return string_to_convert.split(delimiter)

    def model_food_name(self, row):
        """
        Helper method that populates the FoodName model from a csv file
        :param row: a row of data (Creates one instance of the FoodName model)
        """
        if row[0] != "FoodID":
            _, created = FoodName.objects.get_or_create(
                food_id=row[0],
                food_code=row[1],
                food_group_id=row[2],
                food_source_id=row[3],
                food_desc=row[4],
                food_date_of_entry=row[6]
            )
