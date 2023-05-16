from sql import employees_CRUD

def __getAll():
    employees = employees_CRUD.__get_all_employees()

    return employees


def __getBy(search):
    employees = employees_CRUD.__get_by(search)

    return employees


def __getBy_ID(employeeID):
    employees = employees_CRUD.__get_by_id(employeeID)

    return employees


def __insert_into(name, date, salary):
    employees_CRUD.__insert(name, date, salary)


def __delete(employeeID):
    employee = employees_CRUD.__get_by_id(employeeID)

    if not employee:
        raise SystemError("ERRO: FUNCIONARIO NÃO REGISTRADO")
    else:
        employees_CRUD.__delete_id(employeeID)


def __update(employeeID, name, date, salary):
    employee = employees_CRUD.__update_table(employeeID)

    if not employee:
        raise SystemError("ERRO: FUNCIONARIO NÃO REGISTRADO")
    else:
        employees_CRUD.__update_table(employeeID, name, date, salary)

