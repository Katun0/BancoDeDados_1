import sqlite3
from sqlite3 import Error, OperationalError
import os
import Database.createTable as createTable

def __connect_db():
    database = "unoesc.db"
    

    path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(path, database)

    print(f"Buscando banco de dados: {database}")

    if not os.path.isfile(full_path):
        createdb = input(f"Banco de dados não encontrado, deseja criar um novo arquivo SQlite ? [S/N]: ")
        
    connection = sqlite3.connect(full_path)

    if createdb.upper() == 'S':
            option = input("Banco de dados criado com sucesso, deseja criar a tabela 'funcionários ? '")
            if option == 'S':
                print("Tabela Funcionarios criada com sucesso !")
                createTable.create_Table(connection)
            else:
                print("Tabla funcionarios não foi criada !")
    else:
        raise sqlite3.DatabaseError("Banco de dados não selecionado !")

    return connection
    

if __name__ == '__main__':
    conn = None

    try:
        conn = __connect_db()
    except OperationalError as e:
        print('Erro operacional:', e)
    except sqlite3.DatabaseError as e:
        print('Erro database:', e)
    except Error as e:
        print('Erro SQLite3:', e)
    except Exception as e:
        print('Erro durante a execução o sistema!')
        print(e)

    if conn:
        print("Liberando conexão...")
        conn.commit()
        conn.close()

    print("Encerrando")