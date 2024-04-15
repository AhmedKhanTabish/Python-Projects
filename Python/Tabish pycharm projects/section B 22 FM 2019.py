Count = 1
total = 0
while True:
    number = int(input("enter a number"))
    if number > 0:
        total = total + number
        Count = Count + 1
    elif Count < 5:
        print(total)
