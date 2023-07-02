from Database import ConnectDB, createTable

from menu import __menu

def database_init():
  db_connection = ConnectDB.__connect_db()
  createTable.create_Table(db_connection)
  db_connection.close()

def main():
  database_init()
  __menu()
    
main()