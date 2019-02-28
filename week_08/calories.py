# Program:      Lesson 8 Calorie Counter
# Programmer:   Douglas Rosenfield
# Date:         02/26/19
# Purpose:      The purpose of this program is to count the calories of food items based on user input

# banner
print ("welcome to my calorie counter program")

# define variables
cont = ""           # sentinel
item_cnt = int(0)   # item count
tot_cals = int(0)   # total calories

# functions
# displays user options
def disp_menu():
    valid_data = False
    options = "a d q".split()
    while not valid_data:
        print("\nPlease select an option.\n")
        print("a - add")
        print("d - delete")
        print("q - quit")

        seletion = input("> ")
        if selection in options:
            valid_data = True
        else:
            print("That was not a valid option. Please try again.")

# calculates calories based food component grams
def calc_cals(g_type, grams):
    if g_type == "f":
        return grams * 9   
    else:
         return grams * 4

def input_name():
    valid_data = False
    while not valid_data:
        item_name = input("Please enter the item> ")
        if len(item_name) > 20:
            print("Not a valid food name")
        elif len(item_name) == 0:
            print("You must enter a name")
        else:
            valid_data = True

def input_grams(element):
    valid_data = False
    while not valid_data:
        try:
            grams = int(input("Enter grams of {}> ".format(element)))
            valid_data = True
        except Exception as detail:
            print("{} error: ".format(element), detail)

        return grams

# Adds item to meal and updates math for meal
def add_process(tot_cals, item_cnt):
    item_name = input_name()
    g_carbs = input_grams("carbs")
    g_fats = input_grams("fats")
    g_prot = input_grams("protein")
    
    # math
    cals = calc_cals("c", g_carbs) + calc_cals("f", g_fats) + calc_cals("p", g_prot)

    # output
    print("total calories for {} are {}".format(item_name, cals))

    # prompt include item
    incl = input("Would you like to include {}? (y/n)>".format(item_name))

    if incl.lower() == "y":
        add_item(item_name, cals)
        tot_cals = tot_cals + cals
        item_cnt += 1
        print("item {} entered.".format(item_name))
    else:
        print("item {} not entered.".format(item_name))

    return tot_cals, item_cnt


while True:
    choice = disp_menu()
    if choice == "a":
        tot_cals, item_cnt = add_process(tot_cals, item_cnt)
    elif choice == "d":
        del_item()
    elif choice == "q":
        break
    disp_meal()
