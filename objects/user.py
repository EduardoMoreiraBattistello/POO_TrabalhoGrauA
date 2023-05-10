from .album import Album
from .usersticker import UserSticker
from .csvhandler import CSVHandler


class User:
    __collection = None
    
    def __init__(self, username):        
        self.__username = username
        
        self.__album = self.__init_album()
        self.__init_collection()
        
    def __init_album(self) -> Album:
        return Album(1, [], [])
    
    def __init_collection(self):
        self.__collection = CSVHandler.get_userstickers(self.__username)
    
    def add_sticker_to_collection(self, new_sticker: UserSticker):
        sticker = self.__collection.get(new_sticker.get_id())
        
        if sticker is None:
            self.__collection[new_sticker.get_id()] = new_sticker
        else:
            sticker += new_sticker
    
    def get_username(self):
        return self.__username

    def get_album(self) -> Album:
        return self.__album
    
    def get_collection(self) -> list[UserSticker]:
        return self.__collection
    
    @staticmethod
    def register(username: str, password: str) -> bool:
        return CSVHandler.register_user(username, password)    
        
    @staticmethod
    def verify_login(username, password) -> bool:
        user_data = CSVHandler.get_user_data(username)
        if user_data is None:
            return False
        
        return password == user_data["password"]
