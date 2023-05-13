import Database.ConnectDB as ConnectDB


def __get_all_employees():
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = """
    SELECT * FROM funcionarios
    """

    cursor.execute(sql_command)

    employees = cursor.fetchall()

    cursor.close()
    db.close()

    return employees


def __insert(name, date, salary):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = f"""
    INSERT INTO funcionarios VALUES (
    '{name}',
    '{date}',
    '{salary}'
    )
    """

    cursor.execute(sql_command)
    cursor.commit()

    cursor.close()
    db.close()


def __delete_id(employee_id):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = f"""
        DELETE FROM funcionarios WHERE id={employee_id}
    """

    cursor.execute(sql_command)
    db.commit()

    cursor.close()
    db.close()


def __update_table(employee_id, name, date, salary):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = f"""
    UPDATE funcionarios SET
        nome = '{name}',
        data_nascimento = '{date}',
        salario = '{salary}',
    WHERE id={employee_id}
"""
    cursor.execute(sql_command)
    db.commit()

    cursor.close()
    db.close()