#Arquivo principal, onde vai fazer roda o projeto.

from app.logica_sistema import cadastrar_aluno, listar_alunos

comando = ""
while comando != "sair": #para executar continuamente, até sair
    comando = input(f"Escolha uma opção: \n"
                    f"1) Cadastrar Aluno \n"
                    f"2) Listar alunos \n"
                    f"Digite 'sair' para sair do sistema \n")

    match comando:
        case "1": #função de cadastrar o aluno
            nome = input("Informe o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno: ")
            curso = input("Informe o curso do aluno, se tiver. Se não, deixe vazio.")

            print(cadastrar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())

        case "sair":
            print("Saindo do sistema.")