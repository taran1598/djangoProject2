from pathlib import Path, PureWindowsPath
from django.test import TestCase

# Create your tests here.
from data_loader.models import FoodName, NutrientName, NutrientAmount, MeasureName, ConversionFactor
from data_loader.parser import ParserCSV
from website_name.nutrition_label_builder import NutrientLabelBuilder


class NutritionLabelBuilderTest(TestCase):

    def setUp(self) -> None:
        src_file_path_conversion_factor = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\CONVERSION_FACTOR_TEST.csv"))

        src_file_path_food_name = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))

        src_file_path_measure_name = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\MEASURE NAME_TEST.csv"))

        src_file_path_nutrient_amount = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\NUTRIENT_AMOUNT_TEST.csv"))

        src_file_path_nutrient_name = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\NUTRIENT_NAME_TEST.csv"))

        csv_parser = ParserCSV()

        csv_parser.populate_model_from_csv_file_pandas(src_file_path_food_name,
                                                       FoodName.populate_model_food_name_dataframe)
        csv_parser.populate_model_from_csv_file_pandas(src_file_path_nutrient_name,
                                                       NutrientName.populate_model_nutrient_name_dataframe,
                                                       encoding='iso-8859-1')
        csv_parser.populate_model_from_csv_file_pandas(src_file_path_nutrient_amount,
                                                       NutrientAmount.populate_model_nutrient_amount_dataframe,
                                                       encoding='iso-8859-1')
        csv_parser.populate_model_from_csv_file_pandas(src_file_path_measure_name,
                                                       MeasureName.populate_model_measure_name_dataframe,
                                                       encoding='iso-8859-1')
        csv_parser.populate_model_from_csv_file_pandas(src_file_path_conversion_factor,
                                                       ConversionFactor.populate_model_conversion_factor_dataframe,
                                                       encoding='iso-8859-1')

    def test_get_calories_correct(self):
        nutrition_label_builder = NutrientLabelBuilder(food_id=2)

        calories = nutrition_label_builder.getCalories()

    def test_get_food_id_two(self):
        nutrition_label_builder = NutrientLabelBuilder(food_id=2)

        nutrient_info_dictionary = nutrition_label_builder.nutrition_label_builder()

    def test_get_food_id_six(self):
        nutrition_label_builder = NutrientLabelBuilder(food_id=6)

        nutrient_info_dictionary = nutrition_label_builder.nutrition_label_builder()
        x = 1