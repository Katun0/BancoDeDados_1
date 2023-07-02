import Database.ConnectDB as ConnectDB


#Function SQL to search all data on table
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


#Function to search from ID
def __get_by_id(employeeID):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()
    
    sql_command = f"""
    SELECT * FROM funcionarios WHERE
        id = {employeeID}
    """

    cursor.execute(sql_command)

    employee = cursor.fetchall()

    cursor.close()
    db.close()

    return employee


#Function SQL to search from a especific field
def __get_by(search):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = f"""
    SELECT * FROM funcionarios WHERE
        nome LIKE '{search}%' OR
        data_nascimento LIKE '{search}%' OR
        salario LIKE '{search}%'
    """

    cursor.execute(sql_command)
    
    employee = cursor.fetchall()

    cursor.close()
    db.close()

    return employee


#Function SQL to Insert data on table
def __insert(name, date, salary):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = f"""
    INSERT INTO funcionarios(nome, data_nascimento, salario) VALUES (
    '{name}',
    '{date}',
    '{salary}'
    );
    """

    cursor.execute(sql_command)
    db.commit()

    cursor.close()
    db.close()


#Function SQL to Delete data
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


#Function SQL to Uptade data
def __update_table(employee_id, name, date, salary):
    db = ConnectDB.__connect_db()
    cursor = db.cursor()

    sql_command = f"""
    UPDATE funcionarios SET
        nome = '{name}',
        data_nascimento = '{date}',
        salario = '{salary}'
        WHERE id={employee_id}
    """
    cursor.execute(sql_command)
    db.commit()

    cursor.close()
    db.close()