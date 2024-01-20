import mysql.connector
def update_data():
  from Database.display import display_function
  try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password = "admin1",
        database = "my_database"
      )
    
    if mydb.is_connected:
      while True:
        print("Select what you want to change")
        cmd = str(input("(user/password):"))
        
        if cmd.lower() == "user":
          new_user = input("New user: ")
          id_user = int(input("ID: "))
          update_query = "UPDATE users_account SET user = %s WHERE Id = %s;"
          params = (new_user, id_user)
          
          cursor = mydb.cursor()
          cursor.execute(update_query, params)
          mydb.commit()
          print(f"{cursor.rowcount}, has been update")
          
          cursor_sql = mydb.cursor()
          sql = "SELECT * FROM users_account;"
          cursor_sql.execute(sql)
          rows = cursor_sql.fetchall()
          for row in rows:
            print(row)
            
          cursor.close()
          mydb.close()
          display_function()
          break
        else:
          print(f"error no change")
  
  except mysql.connector.Error as err:
    print(f"Error:{err}")