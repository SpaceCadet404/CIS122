# Program:      Lesson 9 Girl Scout Cookies Order Form
# Programmer:   Douglas Rosenfield
# Date:         03/09/2019
# Purpose:      To create an order form using try to validate data in user inputs

# define variables
import locale
locale.setlocale( locale.LC_ALL, '')
order_total = 0.0 #accumulating total for order
price = 3.5 #price of a box of cookies
fmt_price = locale.currency(price, grouping=True)

cookie_list = ("Savannah","Thin-Mints","Tag-a-longs","Peanut-Butter","Sandwich")
order_list = []
detail_list = []

# define functions 

# adds item to cart
def add_process():

    # get flavor
    valid_data = False
    while not valid_data:
        # User cookie choice is recorded
        disp_items()

        try:
            item = int(input("enter item number>"))
            if 1<= item <= len(cookie_list):
                valid_data = True
            else:
                print("\nThat was not a valid choice.")
            
        except Exception as detail:
            print("error: ", detail)

    # get quantity
    valid_data = False
    while not valid_data:
        try:
            qty = int(input("enter quantity> "))

            if 1 <= qty <= 10:
                valid_data = True
            else:
                print ("\nThat was not a valid quantity. Please select between 1 and 10 boxes.")
        except Exception as detail:
            print("error: ", detail)
            print("Please try again. Your entry MUST be an integer.")
    
    item_total = calc_tot(qty)
    fmt_total = locale.currency(item_total, grouping=True)

    print("\nYou chose: {} boxes of {} for a total of {}".format(qty,cookie_list[item-1],fmt_total))
    print()

    # Confirm placing item in order
    valid_data = False
    while not valid_data:
        include = input("Add this to your order? (y/n)> ")
        if include.lower() == "y" or include.lower() == "n":
            if include.lower() == "y":
                inx = item - 1
                
                detail_list = [cookie_list[inx], qty]
                order_list.append(detail_list)

                valid_data = True
                print("{} was added to your order".format(cookie_list[inx]))

            else:
                print("{} was not added to your order".format(cookie_list[inx]))
                valid_data = True
        else:
            print("Please type 'y' or 'n'")
    

# deletes item from cart
def del_item():
    if len(order_list) == 0:
        print("\n** you have no items in your order to delete **\n")
    else:
        print("\nDelete an item")
        disp_order()

        valid_data = False
        while not valid_data:
            try:
                choice = int(input("Please enter the item you would like to delete > "))
                if 1<= choice <= len(order_list):
                    choice = choice - 1
                    print("\nItem {}. {} with {} boxes has been deleted".format(choice+1, cookie_list[choice+1],order_list[choice][1]))
                    order_list.remove(choice)
                    valid_data = True
            except Exception as detail:
                print("Error: ", detail)


# displays cart
def disp_order():
    print("\nYour cart")
    print("Num\tItem\t\tQty\tPrice")
    print("---\t----\t\t---\t-----")
    
    for c in range(len(order_list)):
        print("{}.\t{}\t\t{}\t{}".format(c+1, order_list[c][0], order_list[c][1], order_list[c][1] * 3.5))
        print ("-" * 20)

# displays main control menu
def disp_menu(): 
    options = ["a", "d", "q",]
    while True:
        print("\nPlease select an option:\n")
        print("a - add")
        print("d - delete")
        print("q - quit")

        selection = input("> ")
        if selection in options:
            return selection
        else:
            print("That command was not valid. Please type a command from the menu.") 

def disp_items():
    print("Flavors:")
    for c in range(len(cookie_list)):
        print("{}.\t{}".format(c+1, cookie_list[c]))

    print()

def calc_tot(qty):
    return qty * 3.5
    

#  ____________________ 
# |                    |
# |Active Program here |
# |____________________|

# banner

# main program runs here
while True:
    choice = disp_menu()
    if choice == "a":
        add_process()
    elif choice == "d":
        del_item()
    elif choice == "q":
        break
    disp_order()

disp_order()
print("Thanks for your order!")
