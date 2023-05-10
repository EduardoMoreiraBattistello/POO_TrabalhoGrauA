class Page:
    def __init__(self, title, min_number, max_number):
        self.__sticker = []
        self.__title = title
        self.__min_number = min_number
        self.__max_number = max_number

    def add_sticker(self, sticker):
        self.__sticker.append(sticker)