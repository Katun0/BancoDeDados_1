from uses import employee_use

options = {
    "1": "Listar todos os registros",
    "2": "Cadastrar funcionario",
    "3": "Buscar funcionario por nome, salario ou data",
    "4": "Deletar um registro",
    "5": "Atualizar um registro",
    "0": "Listar todos os registros"
}

def __menu():
    choice = None

    while choice != 0:
        choice = int(input("Escolha uma das opções acima: "))

        try:
            choice = int(input())
        except ValueError:
            raise SystemError("Valor Inválido")
        
        match choice:

            case 1:
                print("Escolha = 1")
            case 2:
                print("Escolha = 1")
            case 3:
                print("Escolha = 1")
            case 4:
                print("Escolha = 1")
            case 5:
                print("Escolha = 1")
            case 0:
                print("Escolha = 1")
