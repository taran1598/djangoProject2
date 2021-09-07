from django.shortcuts import render
from .forms import CsvModelForm
from .models import FoodName, NutrientName, NutrientAmount, MeasureName, ConversionFactor

# Create your views here.
from .parser import ParserCSV


def upload_file_view(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = CsvModelForm(request.POST, request.FILES)
        # check if form is valid
        if form.is_valid():
            form.save()

            # populate the database from the csv files passed in
            populateDatabase(request.FILES)

            # reset form
            form = CsvModelForm()

        return render(request, 'data_loader/upload_page.html', {'form': form})
    else:
        form = CsvModelForm()
        return render(request, 'data_loader/upload_page.html', {'form': form})


# helper methods

def populateDatabase(file_dict):
    """
    Populates database from the csv files in file_dict
    :param file_dict: dictionary containing
    :return:
    """

    parser = ParserCSV()

    try:
        file_dict['food_name_file_name'].file.seek(0)
        file_dict['nutrient_name_file_name'].file.seek(0)
        file_dict['nutrient_amount_file_name'].file.seek(0)
        file_dict['measure_name_file_name'].file.seek(0)
        file_dict['conversion_factor_file_name'].file.seek(0)
        parser.populate_model_from_csv_file_pandas(file_dict['food_name_file_name'].file,
                                                   FoodName.populate_model_food_name_dataframe)
        parser.populate_model_from_csv_file_pandas(file_dict['nutrient_name_file_name'].file, NutrientName.populate_model_nutrient_name_dataframe)
        parser.populate_model_from_csv_file_pandas(file_dict['nutrient_amount_file_name'].file,
                                                   NutrientAmount.populate_model_nutrient_amount_dataframe)
        parser.populate_model_from_csv_file_pandas(file_dict['measure_name_file_name'].file, MeasureName.populate_model_measure_name_dataframe)
        parser.populate_model_from_csv_file_pandas(file_dict['conversion_factor_file_name'].file,
                                                   ConversionFactor.populate_model_conversion_factor_dataframe)

    except KeyError:
        raise KeyError("File is missing")

    # for key, value in file_dict:
    #     if key == 'food_name_file_name':
    #         parser.populate_model_from_csv_file_pandas(value.name, FoodName.populate_model_food_name_dataframe)
    #     elif key == 'nutrient_name_file_name':
    #         parser.populate_model_from_csv_file_pandas(value.name, NutrientName.populate_model_nutrient_name_dataframe)
    #     elif key == 'nutrient_amount_file_name':
    #         parser.populate_model_from_csv_file_pandas(value.name,
    #                                                    NutrientAmount.populate_model_nutrient_amount_dataframe)
    #     elif key == 'measure_name_file_name':
    #         parser.populate_model_from_csv_file_pandas(value.name, MeasureName.populate_model_measure_name_dataframe)
    #     elif key == 'conversion_factor_file_name':
    #         parser.populate_model_from_csv_file_pandas(value.name,
    #                                                    ConversionFactor.populate_model_conversion_factor_dataframe)
