from pathlib import PureWindowsPath, Path

from django.test import TestCase

# Create your tests here.
from data_loader.models import NutrientAmount, FoodName, FoodGroup, ConversionFactor, MeasureName, NutrientName
from data_loader.parser import ParserCSV


class ParserTests(TestCase):

    def test_populate_food_name_pandas(self):
        """
        Tests basic loading of the file into the model
        """
        src_file_path = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                             "Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))
        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path, FoodName.populate_model_food_name_dataframe)
        food_name_objects_count = FoodName.objects.count()
        expected_count = 40
        self.assertEqual(food_name_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {food_name_objects_count:.0f}")

    def test_populate_nutrient_amount_pandas(self):
        """
        Tests basic loading of the file into the model
        """
        src_file_path_nutrient_amt = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                                          "Canadian_Nutrient_Files_Test\\NUTRIENT_AMOUNT_TEST.csv"))

        src_file_path_food_name = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                                       "Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))

        src_file_path_nutrient_name = Path(PureWindowsPath(".\\data_loader\\test_csv_files"
                                                           "\\Canadian_Nutrient_Files_Test\\NUTRIENT_NAME_TEST.csv"))

        # populate data base
        csv_parser = ParserCSV()

        csv_parser.populate_model_from_csv_file_pandas(src_file_path_food_name,
                                                       FoodName.populate_model_food_name_dataframe)

        csv_parser.populate_model_from_csv_file_pandas(src_file_path_nutrient_name,
                                                       NutrientName.populate_model_nutrient_name_dataframe,
                                                       encoding='iso-8859-1')

        csv_parser.populate_model_from_csv_file_pandas(src_file_path_nutrient_amt,
                                                       NutrientAmount.populate_model_nutrient_amount_dataframe)

        # test database has been populated
        nutrient_amount_objects_count = NutrientAmount.objects.count()
        expected_count = 3874
        self.assertEqual(nutrient_amount_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {nutrient_amount_objects_count:.0f}")

    def test_populate_food_group_pandas(self):
        """
        Tests basic loading of the file into the model
        """

        # populate data base
        src_file_path = Path(PureWindowsPath("C:\\Users\\Tarandeep\\Desktop\\website files\\"
                                             "Canadian_Nutrient_Files_Test\\FOOD_GROUP_TEST2.csv"))
        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path,
                                                       FoodGroup.populate_model_food_group_dataframe)

        # test database has been populated
        food_group_objects_count = FoodGroup.objects.count()
        expected_count = 23
        self.assertEqual(food_group_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {food_group_objects_count:.0f}")

    def test_populate_conversion_factor_pandas(self):
        """
        Tests basic loading of the file into the model
        """
        # populate data base
        src_file_path = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\CONVERSION_FACTOR_TEST.csv"))

        src_file_path_food_name = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))

        src_file_path_measure_name = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\MEASURE NAME_TEST.csv"))

        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path_food_name,
                                                       FoodName.populate_model_food_name_dataframe)

        csv_parser.populate_model_from_csv_file_pandas(src_file_path_measure_name,
                                                       MeasureName.populate_model_measure_name_dataframe,
                                                       encoding='iso-8859-1')

        csv_parser.populate_model_from_csv_file_pandas(src_file_path,
                                                       ConversionFactor.populate_model_conversion_factor_dataframe)

        # test database has been populated
        objects_count = ConversionFactor.objects.count()
        expected_count = 172
        self.assertEqual(objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {objects_count:.0f}")

    def test_populate_measure_name_pandas(self):
        """
        Tests basic loading of the file into the model
        """
        # populate data base
        src_file_path = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\MEASURE NAME_TEST.csv"))
        csv_parser = ParserCSV()
        csv_parser.populate_model_from_csv_file_pandas(src_file_path,
                                                       MeasureName.populate_model_measure_name_dataframe,
                                                       encoding='iso-8859-1')

        # test database has been populated
        objects_count = MeasureName.objects.count()
        expected_count = 1162
        self.assertEqual(objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {objects_count:.0f}")
