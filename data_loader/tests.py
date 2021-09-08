import datetime

from pathlib import PureWindowsPath, Path
from django.core.files import File
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from data_loader.forms import CsvModelForm
from data_loader.models import NutrientAmount, FoodName, FoodGroup, ConversionFactor, MeasureName, NutrientName, \
    NutrientCsvFiles
from data_loader.parser import ParserCSV


class ParserTests(TestCase):

    def test_populate_food_name_pandas(self):
        """
        Tests basic loading of the file into the model
        """
        src_file_path = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))

        csv_parser = ParserCSV()
        FoodName.populate_model_food_name_dataframe(csv_parser.populate_model_from_csv_file_pandas(src_file_path,
                                                                                                   encoding='iso-8859-1'))
        food_name_objects_count = FoodName.objects.count()
        expected_count = 40
        self.assertEqual(food_name_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {food_name_objects_count:.0f}")

    def test_populate_nutrient_amount_pandas(self):
        """
        Tests basic loading of the file into the model
        """
        src_file_path_nutrient_amount = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\NUTRIENT_AMOUNT_TEST.csv"))

        src_file_path_food_name = Path(PureWindowsPath(
            ".\\data_loader\\test_csv_files\\Canadian_Nutrient_Files_Test\\FOOD_NAME_TEST.csv"))

        src_file_path_nutrient_name = Path(PureWindowsPath(".\\data_loader\\test_csv_files"
                                                           "\\Canadian_Nutrient_Files_Test\\NUTRIENT_NAME_TEST.csv"))

        # populate data base
        csv_parser = ParserCSV()

        FoodName.populate_model_food_name_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path_food_name, encoding='iso-8859-1'))

        NutrientName.populate_model_nutrient_name_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path_nutrient_name,
                                                           encoding='iso-8859-1'))

        NutrientAmount.populate_model_nutrient_amount_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path_nutrient_amount))

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
        src_file_path = Path(PureWindowsPath(".\\data_loader\\test_csv_files"
                                             "\\Canadian_Nutrient_Files_Test\\FOOD_GROUP_TEST.csv"))
        csv_parser = ParserCSV()
        FoodGroup.populate_model_food_group_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path, encoding='iso-8859-1'))

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
        FoodName.populate_model_food_name_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path_food_name, encoding='iso-8859-1'))

        MeasureName.populate_model_measure_name_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path_measure_name,
                                                           encoding='iso-8859-1'))

        ConversionFactor.populate_model_conversion_factor_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path))

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
        MeasureName.populate_model_measure_name_dataframe(
            csv_parser.populate_model_from_csv_file_pandas(src_file_path, encoding='iso-8859-1'))

        # test database has been populated
        objects_count = MeasureName.objects.count()
        expected_count = 1162
        self.assertEqual(objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {objects_count:.0f}")


class UploadFileViewTests(TestCase):
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

    def test_form_not_valid(self):
        """
        If form is not valid return error stating which part isn't valid
        :return:
        """
        # TODO
        data = {}
        file_data = {}
        form = CsvModelForm(data, file_data)
        self.assertFalse(form.is_valid())

    def test_form_valid(self):
        """
        Form has all fields valid
        :return:
        """
        data = {
            'uploaded': timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59),
            'activated': False
        }

        file_data = {
            'food_name_file_name': File(open(self.src_file_path_food_name)),
            'nutrient_name_file_name': File(open(self.src_file_path_nutrient_name)),
            'nutrient_amount_file_name': File(open(self.src_file_path_nutrient_amount)),
            'measure_name_file_name': File(open(self.src_file_path_measure_name)),
            'conversion_factor_file_name': File(open(self.src_file_path_conversion_factor)),
        }

        form = CsvModelForm(data, file_data)

        self.assertTrue(form.is_valid())

    def test_form_valid_and_objects_populated(self):
        """
        Form has valid data and the data from the form is used to correctly populate Models
        :return:
        """

        data = {
            'uploaded': timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59),
            'activated': False
        }

        file_data = {
            'food_name_file_name': File(open(self.src_file_path_food_name)),
            'nutrient_name_file_name': File(open(self.src_file_path_nutrient_name)),
            'nutrient_amount_file_name': File(open(self.src_file_path_nutrient_amount)),
            'measure_name_file_name': File(open(self.src_file_path_measure_name)),
            'conversion_factor_file_name': File(open(self.src_file_path_conversion_factor)),
        }

        form = CsvModelForm(data, file_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('data_loader:upload'), file_data)

        # test database has been populated

        # test MeasureName model has been populated
        objects_count_measure = MeasureName.objects.count()
        expected_count = 1162
        self.assertEqual(objects_count_measure, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, but found {objects_count_measure:.0f}")

        # test ConversionFactor model has been populated
        objects_count_conversion = ConversionFactor.objects.count()
        expected_count = 172
        self.assertEqual(objects_count_conversion, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, "
                         f"but found {objects_count_conversion:.0f}")

        # test NutrientAmount model has been populated
        nutrient_amount_objects_count = NutrientAmount.objects.count()
        expected_count = 3874
        self.assertEqual(nutrient_amount_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, "
                         f"but found {nutrient_amount_objects_count:.0f}")

        # test FoodName model has been populated
        food_name_objects_count = FoodName.objects.count()
        expected_count = 40
        self.assertEqual(food_name_objects_count, expected_count,
                         f"Expected count of objects to be {expected_count:.0f}, "
                         f"but found {food_name_objects_count:.0f}")

        # test NutrientName model has been populated
        nutrient_name_objects_count = NutrientName.objects.count()
        expected_count = 152
        self.assertEqual(nutrient_name_objects_count,
                         expected_count, f"Expected count of objects to be "
                                         f"{expected_count:.0f}, but found {nutrient_name_objects_count:.0f}")
