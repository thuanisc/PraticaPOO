#Arquivo principal, onde vai fazer roda o projeto.

from app.logica_sistema import cadastrar_aluno, listar_alunos, detalhar_aluno, deletar_aluno

comando = ""
while comando != "sair": #para executar continuamente, até sair
    comando = input(f"Escolha uma opção: \n"
                    f"1) Cadastrar Aluno \n"
                    f"2) Listar alunos \n"
                    f"3) Detalhar aluno \n"
                    f"4) Deletar aluno \n"
                    f"Digite 'sair' para sair do sistema \n")

    match comando:
        case "1": #função de cadastrar o aluno
            nome = input("Informe o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno: ")
            curso = input("Informe o curso do aluno, se tiver. Se não, deixe vazio.")

            print(cadastrar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())

        case "3":
            matricula = input("Informe a matrícula do aluno: ")
            print(detalhar_aluno(matricula))

        case "4":
            matricula = input("Informe a matrícula do aluno: ")
            print(deletar_aluno(matricula))

        case "sair":
            print("Saindo do sistema.")

#como não tem banco de dados, vai zerar a cada run, apenas na memória.