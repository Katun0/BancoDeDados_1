import os
import re

def __title(message):
    print("*" * len(message))
    print(message)
    print("*" * len(message))
    

def __clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def __stop():
    input('Pressione ENTER para continuar...')
    __clean()


def __print_table(employees):
    if employees == None or len(employees) == 0:
        print("Nenhum funcionario registrado")
        return
    
    print(f'{"ID":^5} {"Nome":^25} {"Data de Nascimento":^25} {"Salario":^10}')
    print('-' * 70)

    for c in employees:
        print(f'{c[0]:^5} {c[1]:^25} {c[2]:^25} {c[3]:^10}')



def __parse_input_int(message):
  value = None

  while value == None:
    try:
      value = int(input(f'{message}\n'))
    except:
      print('\n')
      value = None
  
  return value


def __parse_input_float(message):
  value = None

  while value == None:
    try:
      value = float(input(f'{message}\n'))
    except:
      print('\n')
      value = None
  
  return value


def __parse_input_date(message):
  value = None

  while value == None:
    try:
      value = input(f'{message}\n')
      
      if not re.match("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", value):
        raise ValueError
    except:
      print('\n')
      value = None
  
  return value

def get_employee_fields_to_upate(employee):
  fields = [
    { "employee_field": "nome", "message": "do nome", "type": "string" },
    { "employee_field": "data_nascimento", "message": "da data de nascimento", "type": "date" },
    { "employee_field": "salario", "message": "do salário", "type": "float" },
  ]
  
  newEmployee = {
    "nome": employee[0][1],
    "data_nascimento": employee[0][2],
    "salario": employee[0][3],
  }

  print('\n')
  __print_table(employee)
  print('\n')

  for field in fields:
    user_input = input(f'Deseja manter o mesmo valor {field["message"]} (S/N)\n')

    if user_input.lower() != 's':
      new_value_message = f'Digite o novo valor {field["message"]}'
      new_value = None

      if field["type"] == 'data_nascimento':
        print('\n')
        new_value = __parse_input_date(new_value_message)
      elif field["type"] == 'float':
        print('\n')
        new_value = __parse_input_float(new_value_message)
      else:
        new_value = input(f'\n{new_value_message}\n')
      
      newEmployee[field["employee_field"]] = new_value
    
    print('\n')

  return newEmployee