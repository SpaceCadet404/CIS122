# Program:      Lesson 4 Calorie Counter
# Programmer:   Douglas Rosenfield
# Date:         02/01/19
# Purpose:      The purpose of this program is to count the calories of food items based on user input.

# banner
print ("welcome to my calorie counter program")

# define variables
cont = str("y")     # sentinel
item_cnt = int(0)   # item count
tot_cals = int(0)   # total calories


while cont.lower() == "y":
    # capture input
    item_name = input("Please enter the item> ")
    g_carbs = int(input("Enter grams of carbs> "))
    g_fats = int(input("Enter grams of fats> "))
    g_prot = int(input("Enter grams of proteins> "))

    # math below
    cals = (g_carbs * 4) + (g_carbs * 9) + (g_prot * 4)
    
    # accumulate totals
    tot_cals = tot_cals + cals
    item_cnt += 1   # is this different than using " item_cnt = item_cnt + 1 "? Nice and condensed though, better than how I used to do it.

    # output
    print ("Total calories for {} are {}".format(item_name, cals))
    cont = input("Would you like to track another item? (y/n)> ")

print("Your meal has {} items and contains {} calories.".format(item_cnt, tot_cals))
print("Thank you, have a nice day!")
