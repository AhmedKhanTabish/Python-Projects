#                                          Task 1
# Step1: Constant, variable & arrays declaration
# from Mobile_Shop import choice2

phones_code = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL"]
phones_desc = ["     compact                                           ",
               "     clam shell                                        ",
               "     RoboPhone-5 inch screen and 64GB memory           ",
               "     RoboPhone-6 inch screen and 256GB memory          ",
               "     Y-Phone Standard-6 inch screen and 64GB memory    ",
               "     Y-Phone Deluxe-6 inch screen and 256GB memory     "]
phones_price = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99]

tablet_code = ["RTMS", "RTLM", "YTLM", "YTLL"]
tablet_desc = ["     RoboTab-8 inch screen and 64GB memory            ",
               "     RoboTab-10 inch screen and 128GB memory          ",
               "     Y-Tab Standard-10 inch screen and 128GB memory   ",
               "     Y-Tab Deluxe-10 inch screen and 256GB memory     "]
tablet_price = [149.99, 299.99, 499.99, 599.99]

simcard_code = ["SMNO", "SMPG"]
simcard_desc = ["   SIM free       ",
                "   pay as you go  "]
simcard_price = [0.00, 9.99]

CASE_code = ["CSST", "CSLX"]
CASE_desc = ["   standard    ",
             "   luxury      "]
CASE_price = [0.00, 50.00]

charger_code = ["CGCR", "CGHM"]
charger_desc = ["   for car    ",
                "   for home   "]
charger_price = [19.99, 15.99]

output_item_purchased = []
output_total_price = []
total_price = 0.00


# Step 2: Device Selection

def device_selection():
    print()
    print("LIST OF MOBILE PHONES")
    print("Enter Device number(1) for: ", phones_code[0], phones_desc[0], phones_price[0])
    print("Enter Device number(2) for: ", phones_code[1], phones_desc[1], phones_price[1])
    print("Enter Device number(3) for: ", phones_code[2], phones_desc[2], phones_price[2])
    print("Enter Device number(4) for: ", phones_code[3], phones_desc[3], phones_price[3])
    print("Enter Device number(5) for: ", phones_code[4], phones_desc[4], phones_price[4])
    print("Enter Device number(6) for: ", phones_code[5], phones_desc[5], phones_price[5])
    print()
    print("LIST OF TABLETS")
    print("Enter Device number(7) for: ", tablet_code[0], tablet_desc[0], tablet_price[0])
    print("Enter Device number(8) for: ", tablet_code[1], tablet_desc[1], tablet_price[1])
    print("Enter Device number(9) for: ", tablet_code[2], tablet_desc[2], tablet_price[2])
    print("Enter Device number(10) for: ", tablet_code[3], tablet_desc[3], tablet_price[3])
    print()

    choice2 = int(input("Enter the Device number : "))
    if choice2 == 1:
        print("Your choice is BPCM price 29.99")
        output_item_purchased.append(phones_code[0])
        output_total_price.append(float(phones_price[0]))
        # break
    elif choice2 == 2:
        print("Your choice is BPSH price 49.99")
        output_item_purchased.append(phones_code[1])
        output_total_price.append(float(phones_price[1]))
        # break
    elif choice2 == 3:
        print("Your choice is RPSS price 199.99")
        output_item_purchased.append(phones_code[2])
        output_total_price.append(float(phones_price[2]))
        # break
    elif choice2 == 4:
        print("Your choice is RPLL price 499.99")
        output_item_purchased.append(phones_code[3])
        output_total_price.append(float(phones_price[3]))
        # break
    elif choice2 == 5:
        print("Your choice is YPLS price 549.99")
        output_item_purchased.append(phones_code[4])
        output_total_price.append(float(phones_price[4]))
        # break
    elif choice2 == 6:
        print("Your choice is YPLL price 649.99")
        output_item_purchased.append(phones_code[5])
        output_total_price.append(float(phones_price[5]))
        # break
    elif choice2 == 7:
        print("Your choice is RTMS price 149.99")
        output_item_purchased.append(tablet_code[0])
        output_total_price.append(float(tablet_price[0]))
        # break
    elif choice2 == 8:
        print("Your choice is RTLM price 299.99")
        output_item_purchased.append(tablet_code[1])
        output_total_price.append(float(tablet_price[1]))
        # break
    elif choice2 == 9:
        print("Your choice is YTLM price 499.99")
        output_item_purchased.append(tablet_code[2])
        output_total_price.append(float(tablet_price[2]))
        # break
    elif choice2 == 10:
        print("Your choice is YTLL price 599.99")
        output_item_purchased.append(tablet_code[3])
        output_total_price.append(float(tablet_price[3]))
        # break
    return choice2


# Step 3: Sim Card Selection

def sim_selection():
    # from Mobile_Shop import choice1
    print(simcard_code[0], simcard_desc[0], simcard_price[0])
    print(simcard_code[1], simcard_desc[1], simcard_price[1])
    print()

    choice3 = int(input("enter (1) for SIM free or (2) for pay as you go. this is only available for phones : "))

    if choice3 == 1:
        print("Your phone is SIM FREE price 0.00")
        output_item_purchased.append(simcard_code[0])
        output_total_price.append(float(simcard_price[0]))

    elif choice3 == 2:
        print("Your phone has Pay As You Go price 9.99")
        output_item_purchased.append(simcard_code[1])
        output_total_price.append(float(simcard_price[1]))

    # elif choice1 == 1 and choice3 == 2 or 3:
    #     print("your tablet is SIM free. SIM is only for mobiles")
    #     break

    # pass


# Step 4: Case Selection

def case_selection():
    print(CASE_code[0], CASE_desc[0], CASE_price[0])
    print(CASE_code[1], CASE_desc[1], CASE_price[1])
    print()

    choice4 = int(input("enter (1) for CSST standard case price 0.00 or (2) for CSLX luxury case price 50.00 : "))
    if choice4 == 1:
            print("Your choice is CSST price 0.00")
            output_item_purchased.append(CASE_code[0])
            output_total_price.append(float(CASE_price[0]))
    elif choice4 == 2:
            print("Your choice is CSLX price 50.00")
            output_item_purchased.append(CASE_code[1])
            output_total_price.append(float(CASE_price[1]))


# Step 5: Charger Selection

def charger_selection():
    print(charger_code[0], charger_desc[0], charger_price[0])
    print(charger_code[1], charger_desc[1], charger_price[1])
    print()

    choice5 = int(input("enter (1) for CGCR car charger price 19.99 or (2)"
                        " for CGHM home charger price 15.99 or (3) for none or (4) for both "))
    if choice5 == 1:
            print("Your choice is CGCR price 19.99")
            output_item_purchased.append(charger_code[0])
            output_total_price.append(float(charger_price[0]))
    elif choice5 == 2:
            print("Your choice is CGHM price 15.99")
            output_item_purchased.append(charger_code[1])
            output_total_price.append(float(charger_price[1]))
    elif choice5 == 3:
            print("You have not chosen any charger")
    elif choice5 == 4:
            print("Your choice is CGCR price 19.99 and CGHM price 15.99. Total price 35.98")
            output_item_purchased.append(charger_code[0])
            output_total_price.append(float(charger_price[0]))
            output_item_purchased.append(charger_code[1])
            output_total_price.append(float(charger_price[1]))


# Step 6: Price Calculation


def price_calculation(output_total_price):
    return sum(output_total_price)


# Step 7: Printing Output

def printing_output(total):
    print("Items Purchased: ", output_item_purchased)
    print("Items Cost:      ", output_total_price)
    print("Total Amount: ", total)


#                                   Task 2
# Step 8: Repeat Purchase

def repeat_purchase():
    device_selection()
    sim_selection()
    case_selection()
    charger_selection()
    price_calculation(output_total_price)
    # printing_output(total)

    pass


#                                  Task 3
# Step 9: Offering Discount

def discount_offer():

    pass


# Step 10: New Price Calculation

def new_price_calculation():
    pass


# Step 11: Printing New Output

def printing_new_output():
    pass



# Main function
# __name__

condition1 = True

while condition1 == True:
    choice = device_selection()
    if choice <= 6:
        sim_selection()

    case_selection()
    charger_selection()
    total_price = price_calculation(output_total_price)
    printing_output(total_price)
    print("Do you want to purchase more devices:")
    repeat = int(input("Enter (1) to continue more purchase or (2) To Exit : "))
    if repeat == 1:
        condition1 = True
        # repeat_purchase()
        # discount_offer()
        # new_price_calculation()
        # printing_new_output()
        continue
    else:
        break