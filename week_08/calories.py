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
item_list = []      # list of items
cals_list = []      # list of calories for items

# functions
# displays user options
def disp_menu():
    valid_data = False
    options = "a d m q".split()
    while not valid_data:
        print("\nPlease select an option.\n")
        print("a - add")
        print("d - delete")
        print("m - show meal")
        print("q - quit")

        selection = input("> ")
        if selection in options:
            valid_data = True
            return selection
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
            return item_name
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

# Displays meal so far
def disp_meal():
    print("\nMeal Calorie Counter")
    print("Num\tItem\t\tCals")
    print("---\t----\t\t----")
    meal_cals = 0 #accumulator for meal cals

    for c in range(len(item_list)):
        meal_cals += cals_list[c]
        print("{}.\t{}\t\t{}".format(c+1, item_list[c], cals_list[c]))

    print("\nYour meal has {} items for a total of {} calories\n".format(len(item_list), meal_cals))
    print("-" * 20)

# Adds item to lists
def add_item(name, cals):
    item_list.append(name)
    cals_list.append(cals)

# Deletes item from lists
def del_item():
    if len(item_list) == 0:
        print("you have no items in your menu to delete")
    else:
        print("\nDelete an item")
        disp_meal()

        valid_data = False
        while not valid_data:
            try:
                choice = int(input("select an item to delete> ")) - 1
                if 1 <= choice+1 <= len(item_list):
                    print("Item {}. {} with {} calories will be deleted".format(choice + 1, item_list[choice], cals_list[choice]))
                    del item_list[choice]
                    del cals_list[choice]
                    valid_data = True
                else:
                    print("That was not a valid selection.")

            except Exception as detail:
                print("error: ", detail)
                print("please try again")

while True:
    choice = disp_menu()
    if choice == "a":
        tot_cals, item_cnt = add_process(tot_cals, item_cnt)
    elif choice == "d":
        del_item()
    elif choice == "m":
        disp_meal()
    elif choice == "q":
        break
