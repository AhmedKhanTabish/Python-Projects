# question 4 part b


def scanfile(searchstring):
    # filedata : string
    # fileline : integer
    # newdata : string
    nextarrayelement = 1
    fileline = 1
    filedata = readfileline("datafile.txt", fileline)

    while filedata != "":
        if filedata[:7] == searchstring:
            newdata = filedata[7:]
    resultarray[nextarrayelement] = newdata
    nextarrayelement = nextarrayelement + 1
    fileline = fileline + 1
    filedata = readfileline("datafile.txt", fileline)
    scancompleted()  # keyword "call" not valid ???
    return fileline



string = "ahmed20"
x = scan_file(string)
print("file line tabish = ", x)


