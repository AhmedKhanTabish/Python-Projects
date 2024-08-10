

# # this program is to sum up 10 given values
# Total = 0   # total will be the total sum of the numbers
# counter = 0   # counter is to check that only 10 values are given
# number = int(input("enter a number : \n"))
# while True:
#     if counter < 10 and number > 0:
#         Total = Total + number
#         counter = counter + 1
#         print(counter)
#         number = int(input("enter a number : \n"))
#         continue
#     elif counter == 10:
#         print(Total)
#         break



# # this program is to sum up 10 given values
# Total = 0   # total will be the total sum of the numbers
# counter = 0   # counter is to check that only 10 values are given
# number = 0
# while True:
#     if counter < 10 and number >= 0:
#         number = int(input("Enter a positive number : \n"))
#         Total = Total + number
#         print(Total)
#         counter = counter + 1
#         # continue
#     elif number < 0:
#         number = int(input("Negative Numbers not accepted, Enter a positive number : \n"))
#         # continue
#     elif counter == 10:
#         print(Total)
#         break



# this program is to sum up 10 given values
Total = 0   # total will be the total sum of the numbers
counter = 0   # counter is to check that only 10 values are given
number = 0
while True:
    if counter <= 9 and number >= 0:
        Total = Total + number
        number = int(input("Enter a positive number : \n"))
        counter = counter + 1
    elif number < 0:
        number = int(input("Negative Numbers not accepted, Enter a positive number : \n"))
    elif counter == 10:
        Total = Total + number
        print(Total)
        break