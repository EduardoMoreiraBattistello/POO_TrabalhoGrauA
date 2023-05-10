class Trade:
    def __init__(self, biddername, required_sticker, available_sticker):
        self.__biddername = biddername
        self.__required_sticker = required_sticker
        self.__available_sticker = available_sticker
        self.__status = 0

    def swap(self, biddername, required_sticker, available_sticker):
        pass

    def accept(self, accepted):
        pass