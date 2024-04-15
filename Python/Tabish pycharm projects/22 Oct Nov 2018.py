# question 4 part b
def scan_file(search_string):
    print("search_string = ", search_string)
    result_array = []
    next_array_element = 1
    file_line = 1
    file_data = (open("E:/tabish igcse/Tabish pycharm projects/File1.txt", "r").readlines())
    print("file_data:", file_data)
    print(type(file_data))
    # file_data = str(file_data)
    # print(type(file_data))

    while file_data != "":
        print("True")
        print(file_data[:7])
        if search_string == file_data[:7]:
            print("found data")
            search_result = file_data[7:]
            print("search_result=   ", search_result)

            print("search_result=   ", search_result)
            # result_array[next_array_element] = search_result
            # print("result_array=   ", result_array)
            # next_array_element = next_array_element + 1
            # print("next_array_element=   ", next_array_element)
        else:
            print("Not Found")
            break
        file_line = file_line + 1
        file_data = file_data.readlines()
        print('file line in loop = ', file_line)

    print(file_data)
    # file_data.close()
    return file_line


def searchtxt(string):
    with open("file1.txt") as search:
        file_line = 0
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            file_line = file_line + 1
            if string in line:
                print(line)


    return(file_line)






string = "zeeba12"

print(type(string))
print(len(string))
# x = scan_file(string)
y = searchtxt(string)
print("file line tabish = ", y)
