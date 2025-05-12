#MODELS (pasta-padrão para definir modelos de classes)
#geralmente cada classe é feita em um arquivo

import datetime
from uuid import uuid4, uuid4


class Aluno: #tudo o que estiver dentro da identação (espaçamento) é porque está dentro da classe, permitindo o uso do self para puxar as infos
# ATRIBUTOS:

    def __init__(self, nome, nascimento): #def é a função #init inicia a classe #matricula será o Identificador (ID) a ser gerado automáticamente, portanto,não precisa constar aqui
        self.nome = nome #self armazena atributo dentro da variável
        self.nascimento = nascimento
        self.matricula = str(uuid4()) #hash de 24 caracteres que vai variar, sempre sendo único. Não é string, por isso tem que transformar em texto
        self.ingresso = datetime.timezone #puxa o horário do fuso de onde o sistema estiver (CTRL+space+space faz import da biblioteca automaticamente)
        self.curso = None #Quer dizer que existe, mas que ainda não tem valor atribuído
        self.notas = []

# COMPORTAMENTOS:

    def marcar_prova(self, data_prova, nome_prova):
        provas = {} #dicionário para atribuição posterior de valor
        prova = provas.get(nome_prova) #get para puxar

        if not prova: #para lançar uma exceção, caso não tenha prova
            raise Exception #funciona dentro da função, indicativo de tratamento de erro

        prova["data"] = data_prova
        prova["aluno"] = self.matricula

        return f"Sua prova foi marcada para dia {data_prova} com sucesso!"

    def fazer_media(self):
        if not self.notas:
            return "Nenhuma nota fo encontrada."

        media = sum(self.notas)/len(self.notas) #funções built-in, já embutidas no Python. Primeiro soma as notas dentro da lista de notas, depois divide pela quantidade de notas com o len
        return f"Sua média é de {media}." #retorna a resposta pro sistema

    def repor_aula(self, nome_aula):
        aulas_perdidas = {} #dicionário {} é mais próximo ao banco de dados pois pesquisa pelo identificador, já [] lista pesquisa por índice
        aula = aulas_perdidas.get(nome_aula)

        if not aula:
            return "Você já fez esta aula."

        aula["data_reposição"] = data_reposicao
        aula["aluno"] = self.matricula
            return f"Sua aula foi marcada para dia {data_reposicao}."


        pass #passa quando é preenchimento temporário, quer dizer que ainda será feito!