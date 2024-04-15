#                                          Task 1
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

# For selecting Device
choice1 = int(input("enter (0) for phones or (1) for tablet : "))
while True:
    if choice1 == 0:
        print("Enter (1) for: ", phones_code[0], phones_desc[0], phones_price[0])
        print("Enter (2) for: ", phones_code[1], phones_desc[1], phones_price[1])
        print("Enter (3) for: ", phones_code[2], phones_desc[2], phones_price[2])
        print("Enter (4) for: ", phones_code[3], phones_desc[3], phones_price[3])
        print("Enter (5) for: ", phones_code[4], phones_desc[4], phones_price[4])
        print("Enter (6) for: ", phones_code[5], phones_desc[5], phones_price[5])
        break
    elif choice1 == 1:
        print("Enter (7) for: ", tablet_code[0], tablet_desc[0], tablet_price[0])
        print("Enter (8) for: ", tablet_code[1], tablet_desc[1], tablet_price[1])
        print("Enter (9) for: ", tablet_code[2], tablet_desc[2], tablet_price[2])
        print("Enter (10) for: ", tablet_code[3], tablet_desc[3], tablet_price[3])
        break
# For selecting item
choice2 = int(input("enter the number of device : "))
while True:
    if choice2 == 1:
        print("Your choice is BPCM price 29.99")
        output_item_purchased.append(phones_code[0])
        output_total_price.append(float(phones_price[0]))
        break
    if choice2 == 2:
        print("Your choice is BPSH price 49.99")
        output_item_purchased.append(phones_code[1])
        output_total_price.append(float(phones_price[1]))
        break
    if choice2 == 3:
        print("Your choice is RPSS price 199.99")
        output_item_purchased.append(phones_code[2])
        output_total_price.append(float(phones_price[2]))
        break
    if choice2 == 4:
        print("Your choice is RPLL price 499.99")
        output_item_purchased.append(phones_code[3])
        output_total_price.append(float(phones_price[3]))
        break
    if choice2 == 5:
        print("Your choice is YPLS price 549.99")
        output_item_purchased.append(phones_code[4])
        output_total_price.append(float(phones_price[4]))
        break
    if choice2 == 6:
        print("Your choice is YPLL price 649.99")
        output_item_purchased.append(phones_code[5])
        output_total_price.append(float(phones_price[5]))
        break
    if choice2 == 7:
        print("Your choice is RTMS price 149.99")
        output_item_purchased.append(tablet_code[0])
        output_total_price.append(float(tablet_price[0]))
        break
    if choice2 == 8:
        print("Your choice is RTLM price 299.99")
        output_item_purchased.append(tablet_code[1])
        output_total_price.append(float(tablet_price[1]))
        break
    if choice2 == 9:
        print("Your choice is YTLM price 499.99")
        output_item_purchased.append(tablet_code[2])
        output_total_price.append(float(tablet_price[2]))
        break
    if choice2 == 10:
        print("Your choice is YTLL price 599.99")
        output_item_purchased.append(tablet_code[3])
        output_total_price.append(float(tablet_price[3]))
        break

# for selecting Sim card for mobile phones only
while choice1 == 0:
    choice3 = int(input("enter (2) for SIM free or (3) for pay as you go. this is only available for phones : "))

    if choice1 == 0 and choice3 == 2:
        print(simcard_code[0], simcard_desc[0], simcard_price[0])
        print(simcard_code[1], simcard_desc[1], simcard_price[1])
        print("Your phone is SIM FREE price 0.00")
        output_item_purchased.append(simcard_code[0])
        output_total_price.append(float(simcard_price[0]))
        break
    if choice1 == 0 and choice3 == 3:
        print(simcard_code[0], simcard_desc[0], simcard_price[0])
        print(simcard_code[1], simcard_desc[1], simcard_price[1])
        print("Your phone has Pay As You Go price 9.99")
        output_item_purchased.append(simcard_code[1])
        output_total_price.append(float(simcard_price[1]))
        break
    elif choice1 == 1 and choice3 == 2 or 3:
        print("your tablet is SIM free. SIM is only for mobiles")
        break

choice4 = int(input("enter (4) for CSST standard case price 0.00 or (5) for CSLX luxury case price 50.00 : "))
while True:
    if choice4 == 4:
        print(CASE_code[0], CASE_desc[0], CASE_price[0])
        print(CASE_code[1], CASE_desc[1], CASE_price[1])
        print("Your choice is CSST price 0.00")
        output_item_purchased.append(CASE_code[0])
        output_total_price.append(float(CASE_price[0]))
        break
    if choice4 == 5:
        print(CASE_code[0], CASE_desc[0], CASE_price[0])
        print(CASE_code[1], CASE_desc[1], CASE_price[1])
        print("Your choice is CSLX price 50.00")
        output_item_purchased.append(CASE_code[1])
        output_total_price.append(float(CASE_price[1]))
        break

choice5 = int(input("enter (6) for CGCR car charger price 19.99 or (7)"
                    " for CGHM home charger price 15.99 or (8) for none or (9) for both "))
while True:
    if choice5 == 6:
        print(charger_code[0], charger_desc[0], charger_price[0])
        print(charger_code[1], charger_desc[1], charger_price[1])
        print("Your choice is CGCR price 19.99")
        output_item_purchased.append(charger_code[0])
        output_total_price.append(float(charger_price[0]))
        break
    if choice5 == 7:
        print(charger_code[0], charger_desc[0], charger_price[0])
        print(charger_code[1], charger_desc[1], charger_price[1])
        print("Your choice is CGHM price 15.99")
        output_item_purchased.append(charger_code[1])
        output_total_price.append(float(charger_price[1]))
        break
    elif choice5 == 8:
        print("you have not chosen any charger")
        break
    elif choice5 == 9:
        print(charger_code[0], charger_desc[0], charger_price[0])
        print(charger_code[1], charger_desc[1], charger_price[1])
        print("Your choice is CGCR price 19.99 and CGHM price 15.99. Total price 35.98")
        output_item_purchased.append(charger_code[0])
        output_total_price.append(float(charger_price[0]))
        output_item_purchased.append(charger_code[1])
        output_total_price.append(float(charger_price[1]))
        break


print("Items Purchased: ", output_item_purchased)
print("Items Cost:      ", output_total_price)

total_price = sum(output_total_price)
print("Total Amount: ", total_price)

#                                               Task 1 End
#                                               task 2 Start
# choice6 = int(input("Do you want to purchase more  "))
