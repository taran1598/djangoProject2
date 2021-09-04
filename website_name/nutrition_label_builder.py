from django.db.models import Q

from data_loader.models import FoodName, NutrientAmount, FoodGroup, ConversionFactor
from website_name.nutrient_enum import Nutrient


class NutrientLabelBuilder:

    def __init__(self, food_id):
        """
        :param food_id: id of the food to create nutrition label for
        """
        self.food_id = food_id
        # makes sure a FoodName object with food_id exists before trying to get the rest of the attributes from database
        self.validateFoodId()
        self.food_desc = self.getFoodDescription()
        # self.calories , self.serving_size = self.getCalories()
        # self.protein = self.getProtein()
        # self.fat = self.getFats()
        # self.carbohydrates = self.getCarbohydrates()

    def nutrition_label_builder(self):
        """
        Builds the nutrition label from database
        :return: Dictionary where the key is the name of label (ex. calories, total fat, saturated fat, e.t.c) and value
        is the amount
        """

        calories, measure_desc = self.getCalories()
        return {"serving_size": measure_desc,
                "calories": calories,
                "protein": self.getProtein(),
                "fat": self.getFats(),
                "carbohydrates": self.getCarbohydrates()}

    def getCalories(self):
        """
        Get the calorie amount of the food_id. The conversion factor used is defaulted to the first one
        :return: tuple that contains the calorie amount and the measure description (ex. 204, 100g)
        """

        try:
            nutrient_amt_model = self.getNutrientAmountObject(Nutrient.calorie.value)

            conversion_factor_model = self.getConversionFactorModel()

            calories = nutrient_amt_model[0].nutrient_value * conversion_factor_model[0].conversion_factor_value
            measure_description = conversion_factor_model[0].measure_id.measure_description
            # TODO: Remove coupling of measure_description from calorie. Put in own method
            return calories, measure_description

        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} and "
                                              f"nutrient_id: {Nutrient.calorie.value:.0f} does not exist")

    def getCarbohydrates(self) -> int:
        """
        Get the carbohydrate amount of the food_id. The conversion factor used is defaulted to the first one
        :return: int representing carbohydrate amount
        """

        try:
            nutrient_amt_model = self.getNutrientAmountObject(Nutrient.carbohydrate.value)

            conversion_factor_model = self.getConversionFactorModel()

            carbohydrates = nutrient_amt_model[0].nutrient_value * conversion_factor_model[0].conversion_factor_value

            return carbohydrates

        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} and "
                                              f"nutrient_id: {Nutrient.carbohydrate.value:.0f} does not exist")

    def getFats(self) -> int:
        """
        Get the fat amount of the food_id. The conversion factor used is defaulted to the first one
        :return: int representing fat amount
        """

        try:
            nutrient_amt_model = self.getNutrientAmountObject(Nutrient.fat.value)

            conversion_factor_model = self.getConversionFactorModel()

            fat = nutrient_amt_model[0].nutrient_value * conversion_factor_model[0].conversion_factor_value

            return fat

        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} and "
                                              f"nutrient_id: {Nutrient.fat.value:.0f} does not exist")

    def getProtein(self) -> int:
        """
        Get the protein amount of the food_id. The conversion factor used is defaulted to the first one
        :return: int representing the protein amount
        """

        try:
            nutrient_amt_model = self.getNutrientAmountObject(Nutrient.protein.value)

            conversion_factor_model = self.getConversionFactorModel()

            protein = nutrient_amt_model[0].nutrient_value * conversion_factor_model[0].conversion_factor_value

            return protein

        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} and "
                                              f"nutrient_id: {Nutrient.protein.value:.0f} does not exist")

    def getConversionFactorModel(self):
        """
        Gets the ConversionFactor models from the database with self.food_id
        :return: QuerySet of ConversionFactor models
        """
        try:
            return ConversionFactor.objects.filter(Q(food_id=self.food_id), )

        except ConversionFactor.DoesNotExist:
            raise ConversionFactor.DoesNotExist(f"The ConversionFactor object with food_id: {self.food_id:.0f} "
                                                f"does not exist")

    def getNutrientAmountObject(self, nutrient_id):
        """
        Gets QuerySet of NutrientAmount objects with food_id if it exists, otherwise throw NutrientAmount.DoesNotExist error
        :return: Return NutrientAmount objects
        """
        try:
            return NutrientAmount.objects.filter(Q(food_id=self.food_id) &
                                                 Q(nutrient_id=nutrient_id))

        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} "
                                              f"and nutrient_id: {nutrient_id} does not exist")

    def validateFoodId(self):
        """
        Validates whether the FoodName object with food_id exists in the database. Throw error if the object does not
        exist
        """
        try:
            FoodName.objects.get(food_id=self.food_id)
        except FoodName.DoesNotExist:
            raise FoodName.DoesNotExist(f"The food_id: {self.food_id} does not exist")
        except FoodName.MultipleObjectsReturned:
            raise FoodName.MultipleObjectsReturned(f"Multiple FoodName objects were returned for food_id: "
                                                   f"{self.food_id} when only one was suppose to be returned")

    def getFoodDescription(self):
        """
        Gets the description of food_id
        :return: string representing the food description
        """

        try:

            return FoodName.objects.get(pk=self.food_id).food_desc

        except FoodName.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} and "
                                              f"nutrient_id: {Nutrient.protein.value:.0f} does not exist")