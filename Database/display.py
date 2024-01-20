import mysql.connector

# database/display.py
def display_function():
  from main import main_menu 
  from Database.insert import insert_data
  from Database.update import update_data
  from Database.delete import delete_data
  try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password = "admin1",
        database = "my_database"
      )
    if mydb.is_connected:
      while True:
        print("(Title):SQL DATABASE")
        print("(Database):insert/update/delete")
        print("(System):show/back")
        cmd = input("(Users):")
    
        if cmd.lower() == "show":
            cursor = mydb.cursor()
            query = "SELECT * FROM users_account;"
            cursor.execute(query)
            rows = cursor.fetchall()
            
            for row in rows:
              print(row)
        elif cmd.lower() == "insert":
          insert_data()
          break
        elif cmd.lower() == "update":
          update_data()
          break
        elif cmd.lower() == "delete":
          delete_data()
          break
        elif cmd.lower() == "back":
          main_menu()
          break
        else:
            print(f"(System):{cmd}, Invalid syntax.")
      
  except mysql.connector.Error as err:
    print(f"(System): {err}")