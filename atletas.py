'''
Autor: Júlia Carneiro Gonçalves de Souza
Componente Curricular: MI - Algoritmos
Concluido em: 29/11/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
from modalidades import *

class Atletas:
    def __init__(self, nome, idade, sexo, paralisia, covid, modalidade, medalhas, ouro, prata, bronze): #tipos_medalhas):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.paralisia = paralisia
        self.covid = covid
        self.modalidade = modalidade
        self.medalhas = medalhas
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze

    def __repr__(self):
        return f'Modalidade: {self.modalidade.name.capitalize().replace("_", " ")}\nNome: {self.nome.capitalize()}\nIdade: {self.idade}\nSexo: {self.sexo.capitalize()}\nParalisia: {self.paralisia.capitalize()}\nMedalhas' \
               f' conquistadas:\nOuro: {self.ouro}\nPrata: {self.prata}\nBronze: {self.bronze}'

    #valida nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        assert value != '', 'Digite um nome válido.'
        assert not value.isdigit(), 'Digite um nome válido'
        self._nome = value

    #valida idade
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,value):
        assert value.isdigit(), 'Digite uma idade válida'
        assert 0 < int(value) < 100, 'Digite uma idade válida'
        self._idade = value

    #valida sexo
    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        assert ((len(value) > 0) and (value[0] == 'F' or value[0] == 'M')), 'Sexo inválido'
        self._sexo = value[0]

    #valida paralisia
    @property
    def paralisia(self):
        return self._paralisia

    @paralisia.setter
    def paralisia(self, value):
        assert value != '', 'Digite uma paralisia válida'
        assert not value.isdigit(), 'Digite uma paralisia válida.'
        self._paralisia = value

    #valida covid
    @property
    def covid(self):
        return self._covid

    @covid.setter
    def covid(self, value):
        assert ((len(value) > 0) and (value[0] == 'S' or value[0] == 'N')), 'Digite uma opção válida. Foi diagnósticado com COVID? [S/N]'
        #assert not value[0].isnumeric(), 'Digite uma opção válida. Foi diagnósticado com COVID? [S/N]'
        self._covid = True if value[0] == 'S' else False

    #valida modalidade
    @property
    def modalidade(self):
        return self._modalidade

    @modalidade.setter
    def modalidade(self, value):
        assert value.isdigit(), 'Modalidade inválida'
        assert (0 <= int(value) <= 21), 'Modalidade inválida'
        self._modalidade = Modalidades(int(value))

    #valida medalhas
    @property
    def medalhas(self):
        return self._medalhas

    @medalhas.setter
    def medalhas(self, value):
        assert ((len(value) > 0) and (value[0] == 'S' or value[0] == 'N')), 'Digite uma opção válida.Ganhou medalhas? [S/N]'
        self._medalhas = True if value[0] == 'S' else False

    #tipos de medalhas
    @property
    def ouro(self):
        return self._ouro

    @ouro.setter
    def ouro(self, value):
        assert value.isdigit(), 'Entrada inválida. Digite quantas medalhas de ouro ganhou.'
        self._ouro = int(value)

    @property
    def prata(self):
        return self._prata

    @prata.setter
    def prata(self, value):
        assert value.isdigit(), 'Entrada inválida. Digite quantas medalhas de prata ganhou.'
        self._prata = int(value)

    @property
    def bronze(self):
        return self._bronze

    @bronze.setter
    def bronze(self, value):
        assert value.isdigit(), 'Entrada inválida. Digite quantas medalhas de bronze ganhou.'
        self._bronze = int(value)
