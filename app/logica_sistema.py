from models.aluno import Aluno

CURSOS = {} #maiúculo porque é variável global (que pode ser acessada em qualquer função dentro do arquivo)

def cadatrar_aluno(nome, nascimento, curso): #não vai "self" porque não é classe
    if not nome or not nascimento
        return "Parametros inválidos."

    c = {}
    aluno = Aluno(nome, nascimento)

    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno)

        return {
            "nome_aluno": aluno.nome,
            "matricula": aluno.matricula
            "curso": c.get("nome_curso")
        }