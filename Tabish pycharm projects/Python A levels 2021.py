from typing import TextIO


class TreasureChest:
    # private question : String
    # private answer : Integer
    # private points : Integer
    def __init__ (self, question, answer, point):
        self.__question = question
        self.__answer = answer
        self.__point = point
    def read_data(self):
        file_name = "TreasureChestData.txt"
        try:
            file = open(file_name, "r")
        dataFetched = (file.readline()).strip()
        while dataFetched != "":
            question = dataFetched




