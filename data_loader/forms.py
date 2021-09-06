from django import forms
from .models import NutrientCsvFiles


class CsvModelForm(forms.ModelForm):
    class Meta:
        # indicate we want to work on csv model
        model = NutrientCsvFiles
        fields = '__all__'
