import csv

from .csvsticker import CSVSticker
from.usersticker import UserSticker


class CSVHandler:
    @staticmethod
    def get_user_data(username: str):
        with open('users.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if username == row["username"]:
                    return row
        return None
    
    
    @staticmethod
    def register_user(username, password) -> bool:
        if CSVHandler.get_user_data(username):
            return False
        
        with open('users.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, ["username", "password"])
            writer.writerow({"username": username, "password": password})
            
        return True
    
    @staticmethod
    def get_all_stickers():
        with open('stickers.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                yield CSVSticker(row["id"], row["name"], row["content"])
        
    @staticmethod
    def add_usersticker(username, sticker: UserSticker):
        with open('user_stickers.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, ["username", "sticker_id"])
            writer.writerow({"username": username, "sticker_id": sticker.get_id()})
    
    
    @staticmethod
    def get_userstickers(username) -> dict[UserSticker]:
        all_stickers = { sticker.id: sticker for sticker in CSVHandler.get_all_stickers()}
        user_stickers = {}
        
        with open('user_stickers.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if row['username'] != username:
                    continue
                
                csv_sticker = all_stickers[row['sticker_id']]
                
                user_sticker = user_stickers.get(csv_sticker.id)
                if user_sticker is None:
                    user_stickers[csv_sticker.id] = UserSticker.from_csvsticker(csv_sticker)
                else:
                    sticker = UserSticker.from_csvsticker(csv_sticker)
                    user_stickers[csv_sticker.id] += sticker

        return user_stickers