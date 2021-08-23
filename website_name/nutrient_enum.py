from enum import Enum


class Nutrient(Enum):
    # common nutrition label values
    calorie = 208
    protein = 203
    fat = 204
    carbohydrate = 205
    sodium = 307

    caffeine = 262
    # total sugar
    sugars = 269
    fibre = 291

    # sugars
    sucrose = 210
    glucose = 211
    fructose = 212
    lactose = 213
    sorbitol = 261

    # vitamins and minerals
    calcium = 301
    iron = 303
    magnesium = 304
    phosphorus = 305
    potassium = 306
    zinc = 309
    # international units
    vitaminDInternational = 324
    # Vitamin D2 + Vitamin D3
    vitaminD = 328
    vitaminC = 401

    # fatty acids
    transFatTotal = 605
    saturatedFatTotal = 606