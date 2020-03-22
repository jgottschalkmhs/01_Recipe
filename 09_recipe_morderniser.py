# modules to be used
import csv
import re

# ***** Functions ******


def get_all_ingredients():

    all_ingredients = []
    stop = ''
    print("Please enter ingredients one line at a time. Press 'xxx' to when"
          "you are done.")
    while stop != "xxx":

        # Ask user for ingredient (via not blank function)
        get_recipe_line = not_blank("recipe line: ",
                                    "This can't be blank",
                                    "yes")

        # Stop looping if exit code is typed and there are more than 2 ingredients...
        if get_recipe_line.lower() == "xxx" and len(all_ingredients) > 1:
            break
        elif get_recipe_line.lower() == "xxx" and len(all_ingredients) < 2:
            print("You need atleast two ingredients in the list. "
                  "Please add more ingredients.")
        else:
            all_ingredients.append(get_recipe_line)

    return all_ingredients


def not_blank(question, error_msg, num_ok):

    error = error_msg
    response = input(question)
    has_errors = ''
    if num_ok != "yes":
        for letter in response:
            if letter.isdigit() == True:
                has_errors = 'yes'
                break
    if response == "":
        print(error)
        not_blank(question,error_msg,num_ok)
    elif has_errors != '':
        print(error)
        not_blank(question, error_msg, num_ok)

    # return line un-indented by GK as function was returning 'None'
    return response


def num_check(question):
    error = 'please enter a number that is more than zero'
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print('please enter a number that is more than zero ')


def get_sf():
    serving_size = num_check('what is the serving size for the recipe ')


    dodgy_sf = 'yes'
    while dodgy_sf == 'yes':

        desired_size = num_check('how many serving are needed ')
        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: this scale factor is very small "
                             "and you might struggle to accurately weigh"
                             "the ingredients. \n"
                             "do you want to change your serving size? (type 'yes' to change"
                             "your desired serving size )").lower()
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might"
                             "have issues with mixing bowl space / oven space. \n"
                             "Do you want to change your serving size? (type 'yes' to change"
                             "your desired serving size) ").lower()
        else:
            dodgy_sf = 'no'

    return scale_factor

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


def unit_checker(unit_tocheck):

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
    grams = ["g","gram","grams"]

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
    elif unit_tocheck.lower() in litre:
        return "litre"
    elif unit_tocheck.lower() in mls:
        return "mls"
    elif unit_tocheck.lower() in grams:
        return "g"
    else:
        pass

# Main routine
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "ml": 1,
    "g": 1
}

groceries = open('01_ingredients_ml_to_g.csv')

csv_groceries = csv.reader(groceries)

food_dictionary = {}


for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

# set up list to hold 'modernised' ingredients
modernised_recipe =[]

# Ask user for recipe name and check its not blank
recipe_name = not_blank("what is the recipe name? ",
                   "The recipe name can't be blank and can't contain numbers,",
                   "no")

# Ask user where the recipe is originally from (numbers OK)
source = not_blank("where is the recipe from? ",
                   "the source can't be blank, ",
                   "yes")


# Get serving seizes and scale factor
scale_factor = get_sf()

# Get amounts, units and ingredients from user...
full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient...
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"


for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # get amount

    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a sign + sign...
        amount = mixed_num.replace(" ","+")
        # Change the string into a decimal
        amount = eval(amount)
        amount = amount * scale_factor

        # Get unit and ingredient...
        compile_regex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip() # remove extra white space from unit
    else:
        get_amount = recipe_line.split(" ", 1) # split line at first space

        try:
            amount = eval(get_amount[0])  # convert amount to float if possible
            amount = amount * scale_factor

        except NameError:
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    # Get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)  # splits text at first space


    # convert into ml
    num_spaces = recipe_line.count(" ")

    if num_spaces > 1:
        # Item has unit and ingredient
        unit = get_unit[0]
        ingredient = get_unit[1]
        unit = unit_checker(unit)

        # if unit is already in grams, add it to list
        if unit == "g":
            modernised_recipe.append("{:.0f} g {}".format(amount, ingredient))
            continue

        # convert to mls if possible...
        amount = general_converter(amount, unit, unit_central, 1)
        # if we converted to mls, try and convert to grams
        if amount[1] == "yes":
            amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

            # if the ingredient is in the list, convert it
            if amount_2[1] == "yes":
                modernised_recipe.append("{:.0f} g {}".format(amount_2[0], ingredient)) # Rather than printing, update modernised list(g)

            # if the ingredient is not in the list, leave the unit as ml
            else:
                modernised_recipe.append("{.0f} ml {}".format(amount[0], ingredient))
                continue

        # if it's not in mls, leave it unchanged
        else:
            modernised_recipe.append("{:.2f} {} {} ".format(amount[0], unit, ingredient))

    else:
        modernised_recipe.append("{} {}".format(amount,unit_ingredient))


print()
print("*****", recipe_name, "*****")
print()
print("source:",source)
print("Mordernised recipe: ")
for item in modernised_recipe:
    print(item)

