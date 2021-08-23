from django.db.models import Q

from data_loader.models import FoodName, NutrientAmount, FoodGroup, ConversionFactor


class NutrientLabelBuilder:

    def __init__(self, food_id):
        """
        :param food_id: id of the food to create nutrition label for
        """
        self.food_id = food_id
        self.validateFoodId()
        self.nutrient_amount_objects = self.getNutrientAmountObject()

    def getNutrientAmountObject(self):
        """
        Gets NutrientAmount object with food_id if it exists, otherwise throw NutrientAmount.DoesNotExist error
        :return: Return NutrientAmount objects
        """
        try:
            return NutrientAmount.objects.filter(Q(food_id=self.food_id))

        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} "
                                              f"does not exist")

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

    def nutrition_label_builder(self):
        """
        Builds the nutrition label from database
        :return: Dictionary where the key is the name of label (ex. calories, total fat, saturated fat, e.t.c) and value
        is the amount
        """
        nutrition_label_dict = {"serving_size": 0}

    def getFoodDescription(self):
        """
        Returns food description for the given food id
        :return:
        """
        return FoodName.objects.get(food_id=self.food_id)

    def getNutrientAmount(self):
        """
        Queries the NutrientAmount model to retrieve the NutrientAmount objects that had food_id
        :return: Returns list of NutrientAmount models that contain the food_id
        """
        return NutrientAmount.objects.filter(food_id=self.food_id)

    def getFoodGroup(self):
        """
        Finds the food group for the food_id
        :return: FoodGroup object (
        """
        try:
            food_group_id = FoodName.objects.get(pk=self.food_id).food_group_id
            return FoodGroup.objects.get(pk=food_group_id)

        except FoodGroup.MultipleObjectsReturned:
            raise FoodGroup.MultipleObjectsReturned(f"Multiple food groups returned for food_id: {self.food_id:.0f}")
        except FoodName.DoesNotExist:
            raise FoodName.DoesNotExist(f"The food_id : {self.food_id:.0f} does not exist")

    def getCalories(self):
        """
        Get the calorie amount of the food_id. The conversion factor used is defaulted to the first one
        :return: tuple that contains the calorie amount and the measure description (ex. 204, 100g)
        """

        calorie_nutrient_id = 208

        try:
            nutrient_amt_model = NutrientAmount.objects.filter(Q(food_id=self.food_id) &
                                                               Q(nutrient_id=calorie_nutrient_id))

            conversion_factor_model = ConversionFactor.objects.filter(Q(food_id=self.food_id), )

            calories = nutrient_amt_model[0].nutrient_value * conversion_factor_model[0].conversion_factor_value
            measure_description = conversion_factor_model[0].measure_id.measure_description

            return calories, measure_description

        except NutrientAmount.MultipleObjectsReturned:
            raise NutrientAmount.MultipleObjectsReturned(f"Multiple objects were returned with food_id: "
                                                         f"{self.food_id:.0f}")
        except NutrientAmount.DoesNotExist:
            raise NutrientAmount.DoesNotExist(f"The NutrientAmount object with food_id: {self.food_id:.0f} and "
                                              f"nutrient_id: {calorie_nutrient_id:.0f} does not exist")
