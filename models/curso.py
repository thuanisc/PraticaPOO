class Curso: #para funções, o padrão é digitar tudo minúsculo com underline; para classes, primeira letra maiúscula e separações também
#inicializador/chamador do Curso
    def __init__(self, nome, ):
        self.nome = nome #obrigatório definir no inicio
        self.alunos = {} #não é obrigatório definir no início, por isso a lista/dicionário vazio
        self.duracao = duracao
        self.professor = professor
        self.materias = materias
        self.aulas =  []

#comportamentos
    def contabilizar_presenca(self):
        pass

    def listar_alunos_aprovados(self):
        resultado = ""
        for aluno in self.alunos.values():
            if not aluno.notas:
                status = "Sem notas registradas"
            else:
                media = sum(aluno.notas) / len(aluno.notas)
                if media <= 6:
                    status = "Reprovado"
                elif media < 9:
                    status = "Aprovado"
                else:
                    status = "Aprovado com excelência"
            resultado += (f"Nome: {aluno.nome} | Média: {media if aluno.notas else 'N/A'} | Status: {status}\n")
        return resultado or "Nenhum aluno cadastrado no curso."

    def inserir_aluno_no_curso(self, aluno):
        if aluno.matricula in self.alunos:
            return "Este aluno já está neste curso."
        if aluno.curso:
            return "O aluno já está vinculado a outro curso."

        self.alunos[aluno.matricula] = aluno
        aluno.curso = self
        return f"Aluno {aluno.nome} inserido com sucesso no curso {self.nome}."