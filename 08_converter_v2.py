# Conversion Function...

import csv

# ***** Functions go here *****
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"
    else:
        converted = "no"
    return [how_much, converted]

def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t","teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp","tablespoons"]
    cup = ["c", "cup","cups"]
    ounce = ["oz", "fluid", "ounce", "fl-pt","ounces"]
    pint = ["p", "qt", "fl", "gt", "pint","pints"]
    quart = ["q", "qt", "quart", "fl-qt","quarts"]
    pound = ["lb", "#", "pound","pounds"]
    litre = ["litre","liter","l","litres","liters"]
    mls = ["ml","milliliter","millilitre","milliliters","millilitres"]

    if unit_tocheck == "":
        return unit_tocheck
    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck == 'C' or unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in pound:
        return "pound"
    else:
        pass

unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "ml": 1
}

groceries = open('01_ingredients_ml_to_g.csv')

csv_groceries = csv.reader(groceries)

food_dictionary = {}


for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)
keep_going = ''
if __name__ == '__main__':
    while keep_going =='':
        amount = eval(input('How much? '))
        amount = float(amount)

        # Get unit and change it to match dictionary
        unit = unit_checker()
        ingredient = input('Ingredient: ')

        # Convert to mls if possible
        amount = general_converter(amount, unit, unit_central, 1)
        print(amount)

        # If we converted to mls, try and convert to grams
        if amount[1] == "yes":
            amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

            # if the ingredient is in the list, convert it
            if amount_2[1] == "yes":
                print(amount_2)

            # if the ingredient is not in the list, leave the unit as ml
            else:
                print("unchanged")

            # keep_going = input("<enter> or q ")



