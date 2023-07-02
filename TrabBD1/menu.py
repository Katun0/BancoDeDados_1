from uses import employee_use
from utils import functions
from time import sleep

options = {
    "1": "Listar todos os registros",
    "2": "Cadastrar funcionario",
    "3": "Buscar funcionario por nome, salario ou data",
    "4": "Buscar Funcionario por ID",
    "5": "Deletar um registro",
    "6": "Atualizar um registro",
    "0": "Sair do sistema"
}

def __menu():
    choice = None

    while choice != 0:

        print("Selecione uma ação:\n")
        for key, value in options.items():
            print(f'{key} - {value}')
        
        try:
            choice = int(input())
        except ValueError:
            raise SystemError("Valor Inválido")
        
        match choice:

            case 1:
                functions.__title("Listagem de Funcionarios")

                employees = employee_use.__getAll()

                functions.__print_table(employees)
                print('\n')

                functions.__stop()

            
            case 2:
                functions.__title("Cadastro de funcionarios")
                exit = input("Se a opção escolhida não é a desejada, digite 'sair', se não for o seu caso, aperte enter: \n")
                functions.__clean()
                
                if exit.upper() == 'SAIR':
                    print("Retornando ao menu principal.")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal..")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal...")
                    sleep(1)
                    functions.__clean()

                else:
                    name = str(input("Digite o nome do funcionário que deseja cadastrar: "))
                    print("\n")

                    date = functions.__parse_input_date("Digite a data de nascimento do funcionário (ano-mes-dia): ")
                    print("\n")

                    salary = functions.__parse_input_float("Quanto ele recebe por mes?: ")
                    print("\n")

                    print("Inserindo os dados para realizar o cadastro, aguarde um momento...")
                    sleep(5)
                    
                    try:
                        employee_use.insert_into(name, date, salary)
                        print("Cadastro realizado !")
                    except:
                        print("Não foi possível realizar o cadastro !\n")
                
                    functions.__stop()
                        
            case 3:
                functions.__title("Busca de funcionarios por Nome, Salario ou Data de Nascimento")
                exit = input("Se a opção escolhida não é a desejada, digite 'sair', se não for o seu caso, aperte enter: \n")
                functions.__clean()

                if exit.upper() == 'SAIR':
                    print("Retornando ao menu principal.")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal..")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal...")
                    sleep(1)
                    functions.__clean()
                    
                else:
                    
                    search = input("Digite o nome, salario ou data de nascimento do funcionario\n ")
                    employee = employee_use.__getBy(search)

                    print("\n")
                    functions.__print_table(employee)
                    print("\n")

                    functions.__stop()

            case 4:
                functions.__title("Buscar funcionario por ID")
                exit = input("Se a opção escolhida não é a desejada, digite 'sair', se não for o seu caso, aperte enter: \n")
                functions.__clean()
                
                if exit.upper() == "SAIR":
                    print("Retornando ao menu principal.")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal..")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal...")
                    sleep(1)
                    functions.__clean()
                else:
                    employeeID = functions.__parse_input_int("Digite o ID de busca do funcionario: ")

                    employee = employee_use.__getBy_ID(employeeID)
                    
                    print('\n')
                    functions.__print_table(employee)
                    print('\n')

                    functions.__stop()
            
            case 5:
                functions.__title("Deletar um Registro")
                exit = input("Se a opção escolhida não é a desejada, digite 'sair', se não for o seu caso, aperte enter: \n")
                functions.__clean()

                if exit.upper() == 'SAIR':
                    print("Retornando ao menu principal.")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal..")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal...")
                    sleep(1)
                    functions.__clean()

                else:
                    functions.__title("Exclusão de Funcionário")
                    
                    employeeID = functions.__parse_input_int("Digite o ID do funcionario que deseja excluir: ")

                    try:
                        employee_use.__delete(employeeID)
                        print("Funcionário deletado com sucesso \n")
                    except:
                        print("Não foi possível excluir o registro \n")
                
                    functions.__stop()

            case 6:
                functions.__title("Atualizar um registro")
                exit = input("Se a opção escolhida não é a desejada, digite 'sair', se não for o seu caso, aperte enter: \n")
                functions.__clean()

                if exit.upper() == 'SAIR':
                    print("Retornando ao menu principal.")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal..")
                    sleep(1)
                    functions.__clean()
                    print("Retornando ao menu principal...")
                    sleep(1)
                    functions.__clean()
                    
                else:
                    employeeID = functions.__parse_input_int("Digite o ID do funcionario que deseja alterar: ")
                    employee = employee_use.__getBy_ID(employeeID)

                    if len(employee) > 0:
                        newEmployee = functions.get_employee_fields_to_upate(employee)

                        try:
                            employee_use.update(
                                employeeID,
                                newEmployee["nome"],
                                newEmployee["data_nascimento"],
                                newEmployee["salario"],
                                )
                            print('Funcionário alterado com sucesso\n')
                        except:
                            print('\nErro ao alterar funcionário\n')
                    else:
                        print('\nFuncionário não encontrado\n')

                    functions.__stop()
            
