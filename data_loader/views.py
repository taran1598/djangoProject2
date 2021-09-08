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
            ParserCSV.populateDatabase(request.FILES)

            # reset form
            form = CsvModelForm()

        return render(request, 'data_loader/upload_page.html', {'form': form})
    else:
        form = CsvModelForm()
        return render(request, 'data_loader/upload_page.html', {'form': form})


# helper methods
