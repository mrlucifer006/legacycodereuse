from support import *

def login(path, menu):
    users = table(path, ["username", "password"])
    username = input("Username: ")
    password = input("Password: ")
    if ((users["username"] == username) | (users["password"] == password)).any():
        menu()
    else:
        print("Invalid credentials.")

def main():
    while True:
        choice = input("\nQuizWiz\n1 Admin\n2 QuizMaster\n3 Player\n4 Exit\nChoose: ")
        if choice == "1": login(ADMIN, admin_menu)
        elif choice == "2": login(STAFF, staff_menu)
        elif choice == "3": player_menu()
        elif choice == "4": return
        else: print("Invalid option.")

if __name__ == "__main__": main()
