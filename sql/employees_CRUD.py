from Database import ConnectDB

def __get_all_employees():
    db = ConnectDB.connection.__connect_db()
    cursor = db.cursor()

    sql_command = """
    SELECT * FROM funcionarios
    """

    cursor.execute(sql_command)

    employees = cursor.fetchall()

    cursor.close()
    db.close()

    return employees