import os, time, random
from objects import User, CSVHandler, UserSticker, viewalbum


class UI:
    @staticmethod
    def main_menu():
        UI.clear_screen()
        
        while True:
            print('Menu Principal')
            print('1. Novo Album')
            print('2. Acessar Album')
            print('3. Sair')
            
            choice = int(input('Escolha entre (1-3): '))
            
            match (choice):
                case 1:
                    user_username = input('Usuario: ')
                    user_password = input('Senha: ')
                    if not User.register(user_username, user_password):
                        print("Username já cadastrado!")
                        continue
                    
                    print("Registrado com sucesso!")
                    UI.wait()
                    
                    UI.manage_album_screen(User(user_username))
                   
                case 2:
                    user_username = input('Usuario: ')
                    user_password = input('Senha: ')
                    
                    if not User.verify_login(user_username, user_password):
                        print("Usuario ou senha incorretos")
                        UI.wait()
                        continue
                    
                    print("Login com sucesso!")
                    UI.wait()
                    
                    UI.clear_screen()
                    UI.manage_album_screen(User(user_username))
                    
                case 3:
                    break
                
            print()
            
            UI.clear_screen()
            
    @staticmethod
    def manage_album_screen(user: User):
        while True:
            print('Gerenciar Album')
            print('1. Ver album')
            print('2. Gerenciar coleção')
            print('3. Abrir pacote de figurinhas')
            print('4. Voltar ao menu anterior')
            
            choice = int(input('Escolha entre (1-4): '))

            match choice:
                case 1:
                    viewalbum.flip_album()
                case 2:
                    print('Sua coleção de figurinhas: ')
                    for sticker in user.get_collection().values():
                        print(sticker)
                    time.sleep(5)
                case 3:
                    stickers = [*CSVHandler.get_all_stickers()]
                    pack = [random.choice(stickers) for _ in range(3)]
                    
                    print('Suas novas figurinhas: ')
                    for csvsticker in pack:
                        user_sticker = UserSticker.from_csvsticker(csvsticker)
                        
                        user.add_sticker_to_collection(user_sticker)
                        CSVHandler.add_usersticker(user.get_username(), user_sticker)
                        
                        print(csvsticker)
                    time.sleep(5)
                    
                case 4:
                    break
            print()
            UI.clear_screen()
            
    def clear_screen():
        os.system('cls')
    
    def wait():
        time.sleep(1)
    
if __name__ == "__main__":
    UI.main_menu()
