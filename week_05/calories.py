# Program:      Lesson 5 Calorie Counter
# Programmer:   Douglas Rosenfield
# Date:         02/09/19
# Purpose:      The purpose of this program is to count the calories of food items based on user input.

# banner
print ("welcome to my calorie counter program")

# define variables
cont = ""           # sentinel
item_cnt = int(0)   # item count
tot_cals = int(0)   # total calories

while cont.lower() != "y" and cont.lower() != "n":
    cont = input("Would you like to track a meal? (y/n)> ")

while cont.lower() == "y":
    # capture input
    item_name = input("Please enter the item> ")
    g_carbs = int(input("Enter grams of carbs> "))
    g_fats = int(input("Enter grams of fats> "))
    g_prot = int(input("Enter grams of proteins> "))

    # math below
    cals = (g_carbs * 4) + (g_carbs * 9) + (g_prot * 4)
    
    # confirmation of add to meal block here
    valid_data = False  # bool flag
    while not valid_data:
        incl = input("Add {} to your meal? (y/n)> ".format(item_name))
        print()
        if incl.lower() == "y":
            tot_cals = tot_cals + cals
            item_cnt += 1
            print("{} has been added to your meal!\n".format(item_name))
            valid_data = True
        elif incl.lower() == "n":
            print("{} was not added to your meal.\n".format(item_name))
            valid_data = True
        else:
            print("Your input was not valid. Please input either 'y' or 'n'.")

    # output
    print ("Total calories for {} are {}".format(item_name, cals))
    cont = input("Would you like to track another item? (y/n)> ")

print("Your meal has {} items and contains {} calories.".format(item_cnt, tot_cals))
print("Thank you, have a nice day!")
