# record the name and Id of the students according to the First alphabet in the ID
# get info is for getting a valid ID and the name of the student


def get_info():
    id = ""        # ID is An alphabetand four digits 
    valid = False
    while not valid:
        id = input("Please enter a valid ID : ")
        if len(id) == 5 and "A" <= id[0] <= "Z" and id[1:].isnumeric():
            valid = True
    preferred_name = input("Please enter preferred name : ")
    x = id + "*" + preferred_name
    print(x)
    return id + "*" + preferred_name


def write_info(input_data, y):
    f = open(y, "a")
    f.write(input_data)
    return bool


def top_level():
    response = "Y"  # string/character variable
    success = True  # Boolean variable
    while response == "Y":
        input_data = get_info()
        print("Input Data =", input_data)
        print(input_data[0])
        if input_data[0] < "N":
            success = write_info(input_data, "File1.txt")
            print("success1 =", success)
        else:
            success = write_info(input_data, "File2.txt")
            print("success2 =", success)
        if not success:
            response = "Y"
        else:
            response = input("Enter details for another student? (Y/N) ")


top_level()