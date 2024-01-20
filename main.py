# main.py
from Database.display import display_function

def main_menu():
    print("(Title):Main Menu")
    while True:
        user_input = input("Enter a command (database/exit):")

        if user_input.lower() == "database":
            display_function()
            break
        elif user_input.lower() == "exit":
            print("(System):System off")
            break
        else:
            print(f"(System): {user_input}. Invalid syntax.")

if __name__ == "__main__":
    main_menu()