from data_loader.models import FoodName, NutrientAmount, FoodGroup


class NutrientLabelBuilder:

    def __init__(self, food_id):
        """
        :param foodID: id of the food to create nutrition label for
        """
        self.food_id = food_id

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
        return FoodName.objects.get(pk=self.food_id)

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
