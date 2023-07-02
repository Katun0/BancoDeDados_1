

def create_Table(connection):
    cursor = connection.cursor()

    sql_command = """
        CREATE TABLE IF NOT EXISTS funcionarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_nascimento TEXT,
            salario REAL
        );"""

    cursor.execute(sql_command)
    connection.commit()

    if cursor:
        cursor.close()
