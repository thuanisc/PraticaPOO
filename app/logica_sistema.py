from models.aluno import Aluno

CURSOS = {} #maiúculo porque é variável global (que pode ser acessada em qualquer função dentro do arquivo)

def cadatrar_aluno(nome, nascimento, curso): #não vai "self" porque não é classe
    if not nome or not nascimento
        return "Parametros inválidos."

    c = {} #apelido temporário para armazenar informações sobre o curso
    aluno = Aluno(nome, nascimento) #parâmetros já definidos no inicializador no arquivo models/alunos.py #tem que ser na mesma ordem de antes; se quiser trabalhar sem ordem, daí seria (nascimento=nascimento, nome=nome) - pra puxar em qualquer ordem

    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno)

       return {
            "nome_aluno": aluno.nome,
            "matricula": aluno.matricula,
            "curso": c.get("nome_curso")
    }