#Arquivo principal, onde vai fazer roda o projeto.

from app.logica_sistema import (cadastrar_aluno, listar_alunos, detalhar_aluno, deletar_aluno, cadastrar_curso, listar_cursos, detalhar_curso, deletar_curso, inserir_aluno_no_curso)
from app.logica_sistema import CURSOS

comando = ""
while comando != "sair": #para executar continuamente, até sair
    comando = input(f"Escolha uma opção: \n"
                    f"1) Cadastrar Aluno \n"
                    f"2) Listar alunos \n"
                    f"3) Detalhar aluno \n"
                    f"4) Deletar aluno \n"
                    f"5) Cadastrar Curso \n"
                    f"6) Listar Cursos \n"
                    f"7) Detalhar Curso \n"
                    f"8) Deletar Curso \n"
                    f"9) Listar alunos aprovados de um curso \n"
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

        case "5":
            nome = input("Nome do curso: ")
            duracao = input("Duração do curso: ")
            professor = input("Professor responsável: ")
            materias = input("Matérias (separadas por vírgula): ").split(",") if input("Deseja adicionar matérias? (s/n): ").lower() == "s" else None
            print(cadastrar_curso(nome, duracao, professor, materias))

        case "6":
            print(listar_cursos())

        case "7":
            nome = input("Nome do curso: ")
            print(detalhar_curso(nome))

        case "8":
            nome = input("Nome do curso: ")
            print(deletar_curso(nome))

        case "9":
            nome = input("Nome do curso: ")
            curso = CURSOS.get(nome)
            if curso:
                print(curso.listar_alunos_aprovados())
            else:
                print("Curso não encontrado.")

        case "sair":
            print("Saindo do sistema.")

#como não tem banco de dados, vai zerar a cada run, apenas na memória.