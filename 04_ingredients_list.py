# Ingredients List


# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False
    while not valid:

        response = input(question)
        has_errors = ""
        if num_ok != 'yes':
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = 'yes'
                    break

        if response == "":
            print(error_msg)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main Routine...

# Set up empty ingredient list
ingredients = []

# Loop to ask users to enter an ingredient
stop = ''
while stop != 'xxx':
    # Ask user for ingredient (via no blank funcion)
    get_ingredient = not_blank("Please type in an ingredient name: ",
                               "this can't be blank",
                               "yes")
    # If exit code is typed and there are more than 2 ingredients...

    if get_ingredient.lower() == 'xxx' and len(ingredients) > 1:
        break
    elif get_ingredient.lower() =='xxx' and len(ingredients) < 2:
        print('You need at least two ingredients in the list. ',
              'please add more ingredients')
    # if exit code is not entered, add ingredient to list
    else:
        ingredients.append(get_ingredient)

print('Your ingredient list: ',ingredients)













# Output list