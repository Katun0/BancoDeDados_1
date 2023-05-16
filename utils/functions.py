import os

def __title(message):
    print("*" * len(message))
    print(message)
    print("*\n" * len(message))
    

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
        id, name,