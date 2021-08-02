from pathlib import PureWindowsPath, Path

from django.test import TestCase

# Create your tests here.
from data_loader.models import NutrientAmount, FoodName, FoodGroup
from data_loader.parser import ParserCSV


class ParserTests(TestCase):

    def test_populate_food_name_pandas(self):
        src_file_path = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                             "Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))
        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path, FoodName.populate_model_food_name_dataframe)
        food_name_objects_count = FoodName.objects.count()
        expected_count = 40
        self.assertEqual(food_name_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {food_name_objects_count:.0f}")

    def test_populate_nutrient_amount_pandas(self):
        src_file_path = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                             "Canadian_Nutrient_Files_Test\\NUTRIENT_AMOUNT_TEST.csv"))
        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path,
                                                       NutrientAmount.populate_model_nutrient_amount_dataframe)
        nutrient_amount_objects_count = NutrientAmount.objects.count()
        expected_count = 3874
        self.assertEqual(nutrient_amount_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {nutrient_amount_objects_count:.0f}")

    def test_populate_food_group_pandas(self):
        src_file_path = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                             "Canadian_Nutrient_Files_Test\\FOOD_GROUP_TEST2.csv"))
        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path,
                                                       FoodGroup.populate_model_food_group_dataframe)
        food_group_objects_count = FoodGroup.objects.count()
        expected_count = 23
        self.assertEqual(food_group_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {food_group_objects_count:.0f}")
