import mysql.connector
def insert_data():
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
          print("(Title):INSERT DATABASE")
          print("(Database):user/password")

          user_acc = str(input("(user):"))
          pass_acc = str(input("(password):"))
          account = (user_acc,pass_acc)
            
          cursor = mydb.cursor()
          insert_query = "INSERT INTO users_account (user,password) VALUES (%s, %s);"
          cursor.execute(insert_query,account)
          mydb.commit()
          print(f"(Database): {cursor.rowcount}, record inserted!")
          
          cursor_display = mydb.cursor()
          sql = "SELECT * FROM users_account;"
          cursor_display.execute(sql)
          rows = cursor_display.fetchall()
          for row in rows:
            print(row)
          
          cursor.close()
          mydb.close()
          display_function()
          break
    except mysql.connector.Error as err:
      print(err)