from models.aluno import Aluno

def cadatrar_aluno(nome, nascimento, curso): #não vai "self" porque não é classe
    if not nome or not nascimento
        return "Parametros inválidos."

    aluno = Aluno(nome, nascimento)