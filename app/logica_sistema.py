from models.aluno import Aluno #vai importar a classe Aluno e suas informações já pré-definidas da pasta models/aluno

CURSOS = {} #maiúculo porque é variável global (que pode ser acessada em qualquer função dentro do arquivo)
ALUNOS = []

def cadastrar_aluno(nome, nascimento, curso): #não vai "self" porque não é classe
    if not nome or not nascimento:
        return "Parametros inválidos."

    c = {} #apelido temporário para armazenar informações sobre o curso
    aluno_objeto = Aluno(nome, nascimento) #parâmetros já definidos no inicializador no arquivo models/alunos.py #tem que ser na mesma ordem de antes; se quiser trabalhar sem ordem, daí seria (nascimento=nascimento, nome=nome) - pra puxar em qualquer ordem #curso é opcional, por isso o None

    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno_objeto)

    ALUNOS.append(aluno_objeto)

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.get("nome_curso")
    }

def listar_alunos():
    resposta = "" #para a resposta ser uma string
    for aluno in ALUNOS:
        resposta += (f"\n Nome: {aluno.nome}\n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso} \n"
                     f"_______________________ \n") #cada vez que executar, vai add um aluno

    return resposta


