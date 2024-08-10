
password = int(input("enter the correct password:\n "))

while True:
    if password < 100:
        password = int(input("Try again:\n "))
        continue
    elif password == 100:
        password = int(input("Try again ..... you are very close:\n "))
        continue
    elif password > 100:
        print("entry accepted")
        break