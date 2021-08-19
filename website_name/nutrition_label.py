

class NutritionLabel:

    # TODO: CREATE DATABASE MODEL
    def __init__(self, serving_size, calories, total_fat, saturated_fat, unsaturated_fat, trans_fat, cholesterol,
                 total_carbs, dietary_fiber, total_sugar, added_sugar, protein, *args):
        self.serving_size = serving_size
        self.calories = calories
        self.total_fat = total_fat