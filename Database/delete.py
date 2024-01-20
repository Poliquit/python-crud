import mysql.connector

def delete_data():
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
        cmd = int(input("(Select ID): "))
        placeholder = (cmd,)
        cursor = mydb.cursor()
        delete_query = "DELETE FROM users_account WHERE Id = %s;"
        cursor.execute(delete_query, (placeholder))
        mydb.commit()
        print(f"ID: {cursor.rowcount}, has been deleted")
        
        display_function()
        break
  except mysql.connector.Error as err:
    print(f"Error:{err}")