# question 4 part b
def scan_file(search_string):
    print("search_string = ", search_string)
    result_array = []
    next_array_element = 1
    file_line = 1
    file_data = open("E:/tabish igcse/Tabish pycharm projects/File1.txt", "r")
    file_data.readline()
    print("file_data = ", file_data.readline())
    # while file_data != "":
    #     # if file_data[0:6] == search_string:
    #     #     result_array[next_array_element] = file_data
    #     #     next_array_element = next_array_element + 1
    #     file_line = file_line + 1
    #     # file_data = file_data.readlines()
    #     print('file line in loop = ', file_line)
    print(file_data.readline())

    file_data.close()
    return file_line


string = "ahmed20"
x = scan_file(string)
print("file line = ", x)


