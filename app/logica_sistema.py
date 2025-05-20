from models.aluno import Aluno #vai importar a classe Aluno e suas informações já pré-definidas da pasta models/aluno
from models.curso import Curso

CURSOS = {} #maiúculo porque é variável global (que pode ser acessada em qualquer função dentro do arquivo)
ALUNOS = {} #variável global

def cadastrar_aluno(nome, nascimento, nome_curso=None): #não vai "self" porque não é classe
    if not nome or not nascimento:
        return "Parametros inválidos."

    c = None #apelido temporário para armazenar informações sobre o curso #fica None (vazio) mesmo, para receber depois o parâmetro
    aluno_objeto = Aluno(nome, nascimento) #parâmetros já definidos no inicializador no arquivo models/alunos.py #tem que ser na mesma ordem de antes; se quiser trabalhar sem ordem, daí seria (nascimento=nascimento, nome=nome) - pra puxar em qualquer ordem #curso é opcional, por isso o None

    if nome_curso:
        c = CURSOS.get(nome_curso)
        c.alunos[aluno_objeto.matricula] = aluno_objeto

    ALUNOS[aluno_objeto.matricula] = aluno_objeto #salva na variável global o aluno cadastrado, simulando um banco de dados

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.nome or None #O c virou objeto da Classe curso e puxará seu .nome OU pode ser vazio. Caso não defina que pode ser vazio, dará erro.
    }

def listar_alunos():
    resposta = "" #para a resposta ser uma string

    if not ALUNOS:
        print("Nenhum aluno cadastrado.")

    for aluno in ALUNOS.values():
        resposta += (f"\n Nome: {aluno.nome}\n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso.nome if aluno.curso else "Sem curso no momento"} \n" #pega informação do curso a partir da Classe aluno
                     f"_______________________ \n") #cada vez que executar, vai add um aluno

    return resposta

def detalhar_aluno(matricula):
    if not matricula:
        return "Parâmetros inválidos."

    aluno = ALUNOS.get(matricula)
    if not aluno:
        return "Este aluno não está cadastrado"

    return (f"Nome: {aluno.nome}\n"
            f"Matrícula: {aluno.matricula}\n"
            f"Data de nascimento: {aluno.nascimento}\n"
            f"Data de ingresso: {aluno.ingresso}\n"
            f"Curso: {aluno.curso.nome if aluno.curso else "Sem curso no momento"}\n"
            f"Notas: {aluno.notas}")

def deletar_aluno(matricula):
    if not matricula:
        return "Parâmetros inválidos"

    aluno = ALUNOS.get(matricula)
    if not aluno:
        return "Este aluno não está cadastrado"

    if aluno.curso: #tem que ter essa verificação, pois nem sempre um aluno cadastrado terá curso cadastrado, então para evitar erro só remove se (if) tiver
        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)
    return "Aluno excluído com sucesso"

# NOVAS FUNÇÕES DE CURSO

def cadastrar_curso(nome, duracao=None, professor=None, materias=None):
    if not nome:
        return "Nome do curso é obrigatório."

    if nome in CURSOS:
        return "Este curso já está cadastrado."

    curso = Curso(nome, duracao, professor, materias)
    CURSOS[nome] = curso
    return f"Curso '{nome}' cadastrado com sucesso!"

def listar_cursos():
    if not CURSOS:
        return "Nenhum curso cadastrado."
    resultado = ""
    for curso in CURSOS.values():
        resultado += (f"\nCurso: {curso.nome}\n"
                      f"Professor: {curso.professor or 'Não informado'}\n"
                      f"Duração: {curso.duracao or 'Não informada'}\n"
                      f"Alunos: {len(curso.alunos)}\n"
                      f"_______________________\n")
    return resultado

def detalhar_curso(nome):
    curso = CURSOS.get(nome)
    if not curso:
        return "Curso não encontrado."

    return (f"Curso: {curso.nome}\n"
            f"Professor: {curso.professor or 'Não informado'}\n"
            f"Duração: {curso.duracao or 'Não informada'}\n"
            f"Matérias: {curso.materias if curso.materias else 'Nenhuma'}\n"
            f"Quantidade de alunos: {len(curso.alunos)}")

def deletar_curso(nome):
    curso = CURSOS.get(nome)
    if not curso:
        return "Curso não encontrado."

    if curso.alunos:
        return "Não é possível excluir um curso com alunos vinculados."

    CURSOS.pop(nome)
    return f"Curso '{nome}' excluído com sucesso!"

def inserir_aluno_no_curso(matricula_aluno, nome_curso):
    if not matricula_aluno or not nome_curso:
        return "Parâmetros inválidos."

    aluno = ALUNOS.get(matricula_aluno)
    if not aluno:
        return "Aluno não encontrado."

    curso = CURSOS.get(nome_curso)
    if not curso:
        return "Curso não encontrado."

    # Verifica se o aluno já está em um curso e remove do curso anterior
    if aluno.curso:
        curso_anterior = CURSOS.get(aluno.curso.nome)
        if curso_anterior:
            curso_anterior.alunos.pop(matricula_aluno, None)

    # Atualiza curso do aluno e adiciona aluno ao curso
    aluno.curso = curso
    curso.alunos[matricula_aluno] = aluno

    return f"Aluno '{aluno.nome}' inserido no curso '{curso.nome}' com sucesso."