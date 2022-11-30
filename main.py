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
from atletas import *
from time import sleep
import jsonpickle
import os


def cadastrar_atletas(dicio_atletas):
    continuar = 'S'
    while continuar in 'S':
        nome = input('Digite seu nome: ').strip().upper()
        idade = input('Digite sua idade: [1-99]').strip()
        sexo = input('Digite seu sexo: [F/M] ').strip().upper()
        paralisia = input('Digite qual a sua paralisia: ')
        covid = input('Teve covid? ').strip().upper()
        modalidade = input('Qual modalidade você participa? ').strip()
        medalhas = input('Você ganhou medalhas? ').strip().upper()
        if medalhas in 'SSIM':
            ouro = input('Quantas de ouro? ').strip()
            prata = input('Quantas de prata? ').strip()
            bronze = input('Quantas de bronze? ').strip()
        else:
            ouro = '0'
            prata = '0'
            bronze = '0'
        if nome in dicio_atletas.keys():
            print('Atleta já cadastrado')
        else:
            try:
                atleta = Atletas(nome, idade, sexo, paralisia, covid, modalidade, medalhas, ouro, prata, bronze)
                dicio_atletas[atleta.nome] = atleta

                print('Cadastrado com sucesso!')
            except Exception as e:
                print(e)

        continuar = input('Deseja cadastrar mais atletas? ').strip().upper()
        while continuar not in 'SN' or continuar == '':
            continuar = input('Opção não reconhecida. Deseja cadastrar mais atletas? [S/N] ').strip().upper()

    return dicio_atletas


def alterar_cadastro(dicio_atletas):
    atleta_alterar = input('Digite o nome do atleta que quer alterar: ').strip().upper()
    while atleta_alterar.isdigit() or atleta_alterar == '':
        atleta_alterar = input('Digite um nome válido: ')

    if atleta_alterar in dicio_atletas.keys():

        atributo = input('O que deseja alterar?\n1-Nome\n2-Idade\n3-Sexo\n4-Tipo de paralisia\n'
                         '5-Diagnóstico de COVID\n6-Medalhas ganhas\n7-Modalidade\n')
        while atributo not in '1234567' or atributo == '':
            atributo = input('O que deseja alterar?\n1-Nome\n2-Idade\n3-Sexo\n4-Tipo de paralisia\n'
                             '5-Diagnóstico de COVID\n6-Medalhas ganhas\n7-Modalidade\n')

        if atributo == '1':
            novo_nome = input('Digite o novo nome: ').strip().upper()
            while novo_nome.isdigit() or novo_nome == '':
                novo_nome = input('ERRO. Digite o novo nome: ').strip().upper()

            dicio_atletas[atleta_alterar].nome = novo_nome
            dicio_atletas[novo_nome] = dicio_atletas.pop(atleta_alterar)
            print('Alteração realizada!')

        elif atributo == '2':
            nova_idade = input('Digite a nova idade: [1-99]')
            while not nova_idade.isdigit() or (not 0 < int(nova_idade) < 100):
                nova_idade = input('ERRO. Digite a nova idade: [1-99]')
                print(nova_idade)
            print(nova_idade)
            dicio_atletas[atleta_alterar].idade = nova_idade
            print('Alteração realizada!')

        elif atributo == '3':
            novo_sexo = input('Digite o novo sexo: ').strip().upper()
            while novo_sexo.isdigit() or novo_sexo == '':
                novo_sexo = input('ERRO. Digite o novo sexo: [F/M] ').strip().upper()
            dicio_atletas[atleta_alterar].sexo = novo_sexo
            print('Alteração realizada!')

        elif atributo == '4':
            nova_paralisia = input('Digite a nova paralisia: ').strip().upper()
            while nova_paralisia.isdigit() or nova_paralisia == '':
                nova_paralisia = input('ERRO. Digite a nova paralisia: ').strip().upper()
            dicio_atletas[atleta_alterar].paralisia = nova_paralisia
            print('Alteração realizada!')

        elif atributo == '5':
            novo_covid = input('Digite o novo diagnóstico: [S/N]').strip().upper()
            while novo_covid.isdigit() or novo_covid == '':
                novo_covid = input('ERRO. Digite o novo diagnóstico: [S/N] ').strip().upper()
            dicio_atletas[atleta_alterar].covid = novo_covid
            print('Alteração realizada!')

        elif atributo == '6':
            novas_medalhas = input('Você ganhou medalhas? [S/N] ').strip().upper()
            while novas_medalhas.isdigit() or novas_medalhas == '':
                novas_medalhas = input('ERRO. Você ganhou medalhas? [S/N] ').strip().upper()
            dicio_atletas[atleta_alterar].medalhas = novas_medalhas
            if novas_medalhas in 'SSIM':
                novo_ouro = input('Quantas de ouro? ').strip()
                novo_prata = input('Quantas de prata? ').strip()
                novo_bronze = input('Quantas de bronze? ').strip()
                while not novo_ouro.isdigit() or not novo_prata.isdigit() or not novo_bronze.isdigit():
                    print('ERRO! Digite novamente as novas medalhas: ')
                    novo_ouro = input('Quantas de ouro? ').strip()
                    novo_prata = input('Quantas de prata? ').strip()
                    novo_bronze = input('Quantas de bronze? ').strip()
                dicio_atletas[atleta_alterar].ouro = novo_ouro
                dicio_atletas[atleta_alterar].prata = novo_prata
                dicio_atletas[atleta_alterar].bronze = novo_bronze
                print('Alteração realizada!')
            else:
                dicio_atletas[atleta_alterar].ouro = '0'
                dicio_atletas[atleta_alterar].prata = '0'
                dicio_atletas[atleta_alterar].bronze = '0'
                print('Alteração realizada!')

        else:
            nova_modalidade = input('Digite a nova modalidade: ')
            while (not nova_modalidade.isdigit() or nova_modalidade == '') or (not 0 <= int(nova_modalidade) <= 21):
                nova_modalidade = input('ERRO! Digite a nova modalidade: ')
            dicio_atletas[atleta_alterar].modalidade = nova_modalidade
            print('Alteração realizada!')
    else:
        print('Atleta não encontrado no sistema.')


def excluir_cadastro(dicio_atletas):
    atleta_deletar = input('Digite o nome do atleta que quer deletar: ').strip().upper()
    while atleta_deletar.isdigit() or atleta_deletar == '':
        atleta_deletar = input('Digite um nome válido: ')
    if dicio_atletas != {} and atleta_deletar in dicio_atletas.keys():
        dicio_atletas.pop(atleta_deletar)
        print('Cadastro removido com sucesso!')

    else:
        print('Não foi possível executar a remoção de cadastro.')


#QUESTÕES
#Q1 / Q2 E PRINTS DE AMBAS
def quantidade_atletas(dicio_atletas):
    atletas_fem = [0 for modalidade in range(22)]  #codigo discutido na sessão 3 - 11/11/2021
    atletas_masc = [0 for modalidade in range(22)]

    for atleta in dicio_atletas.values():
        if atleta.sexo == 'F':
            atletas_fem[atleta.modalidade.value] += 1
        else:
            atletas_masc[atleta.modalidade.value] += 1

    soma_atletas = len(dicio_atletas)

    return atletas_fem, atletas_masc, soma_atletas


def quantidade_atletas_covid(dicio_atletas):
    covid_fem = [0 for modalidade in range(22)]  #mesma lógica codigo discutido na sessão 3 - 11/11/2021
    covid_masc = [0 for modalidade in range(22)]

    for atleta in dicio_atletas.values():
        if atleta.covid:
            if atleta.sexo == 'F':
                covid_fem[atleta.modalidade.value] += 1
            else:
                covid_masc[atleta.modalidade.value] += 1

    soma_covid = (sum(covid_fem) + sum(covid_masc))

    return covid_fem, covid_masc, soma_covid


def quantidades(dicio_atletas):
    atletas_fem, atletas_masc, soma_atletas = quantidade_atletas(dicio_atletas)
    covid_fem, covid_masc, soma_covid = quantidade_atletas_covid(dicio_atletas)

    return atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid


#printar ambas quantidades, total e com covid
def printar_quantidades(atletas_fem, atletas_masc, soma_atletas):
    #função para printar corretamente a quantidade de atletas e atletas com covid
    titulo = ' QUANTIDADE DE ATLETAS '
    print(titulo.center(40, '='))
    print(f'O total de atletas foi: {soma_atletas}') #a soma_atletas é o len(dicio_atletas) que foi definido na função quantidade_atletas
    if sum(atletas_fem) != 0:
        print(f'{sum(atletas_fem)} atletas do sexo feminino, nas respectivas modalidades: ')
        for i in Modalidades:
            if atletas_fem[i.value] != 0:
                print(f'{i.name.capitalize().replace("_"," ")}: {atletas_fem[i.value]}')
                sleep(0.2)
    if sum(atletas_masc) != 0:
        print(f'{sum(atletas_masc)} atletas do sexo masculino, nas respectivas modalidades:')
        for i in Modalidades:
            if atletas_masc[i.value] != 0:
                print(f'{i.name.capitalize().replace("_"," ")}: {atletas_masc[i.value]}')
                sleep(0.2)
    print()  #apenas para espaçamento entre prints


def printar_covid(covid_fem, covid_masc, soma_covid):
    titulo = ' QUANTIDADE DE ATLETAS COM COVID '
    print(titulo.center(50, '='))
    print(f'O total de atletas com COVID foi: {soma_covid}')  #soma_covid é a soma de ambas as listas, que foi calculada na função quantidade_atletas_covid
    if sum(covid_fem) != 0:  #não fiz um if soma_covid != 0 para caso um dos sexos seja 0 e outro não, dessa forma, printando apenas o que teve atletas.
        print(f'{sum(covid_fem)} atletas do sexo feminino, nas respectivas modalidades: ')
        for i in Modalidades:
            if covid_fem[i.value] != 0:
                print(f'{i.name.capitalize().replace("_", " ")}: {covid_fem[i.value]}')
                sleep(0.2)
    if sum(covid_masc) != 0:
        print(f'{sum(covid_masc)} atletas do sexo masculino, nas respectivas modalidades:')
        for i in Modalidades:
            if covid_masc[i.value] != 0:
                print(f'{i.name.capitalize().replace("_", " ")}: {covid_masc[i.value]}')
                sleep(0.2)
    print()
def prints_quant_atletas(atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid):
    printar_quantidades(atletas_fem, atletas_masc, soma_atletas)
    printar_covid(covid_fem, covid_masc, soma_covid)

#Q3
def quadro_medalhas(dicio_atletas):
    #código discutido na sessão 5 - 25/11/2021
    teve_medalhas = False
    matriz_medalhas = [[0 for medalhas in range(3)] for modalidades in range(22)]  #gera uma matriz correspondente a 22 modalidades e 3 tipos de medalhas
    for atleta in dicio_atletas.values():
        if atleta.medalhas:
            matriz_medalhas[atleta.modalidade.value][0] += atleta.ouro
            matriz_medalhas[atleta.modalidade.value][1] += atleta.prata
            matriz_medalhas[atleta.modalidade.value][2] += atleta.bronze
            teve_medalhas = True
    return matriz_medalhas, teve_medalhas

def print_quadro_medalhas(matriz_medalhas, teve_medalhas):
    if teve_medalhas: #para só printar o titulo se houver medalhas
        titulo = ' QUADRO DE MEDALHAS '
        print(titulo.center(40, '='))
        for modalidade in Modalidades: #print seguindo o mesmo modelo da função printar_quant_atletas
            if sum(matriz_medalhas[modalidade.value]) != 0:
                print(f'{modalidade.name.capitalize().replace("_", " ")}:\nOuro: {matriz_medalhas[modalidade.value][0]}\nPrata: {matriz_medalhas[modalidade.value][1]}\nBronze: {matriz_medalhas[modalidade.value][2]}\n')
                sleep(0.2)

#Q4
def relatorio_atleta(dicio_atletas, teve_medalhas):
    if teve_medalhas:
        titulo = ' RELATÓRIO DOS MEDALHISTAS '
        print(titulo.center(40, '='))
        for i in Modalidades:
            for atleta in dicio_atletas.values():
                if (atleta.modalidade and atleta.modalidade == i) and (atleta.sexo == 'F'): #primeiro as mulheres serão printadas.
                    print(f'{atleta}\n')
                    sleep(0.2)

        for i in Modalidades:
            for atleta in dicio_atletas.values():
                if (atleta.modalidade and atleta.modalidade == i) and (atleta.sexo == 'M'): #depois os homens.
                    print(f'{atleta}\n')
                    sleep(0.2)

#Q5
def participacao_brasil(dicio_atletas, matriz_medalhas):
    modalidade_medalhas = []
    modalidade_sem_medalhas = []
    modalidade_nao_participou = []

    for atleta in dicio_atletas.values():
        if atleta.medalhas:
            for modalidade in Modalidades:
                if (sum(matriz_medalhas[modalidade.value]) != 0) and (modalidade.name not in modalidade_medalhas):
                    modalidade_medalhas.append(modalidade.name)
        else:
            for modalidade in Modalidades:
                if (atleta.modalidade.value == modalidade.value) and (modalidade.name not in modalidade_medalhas) and (modalidade.name not in modalidade_sem_medalhas):
                    modalidade_sem_medalhas.append(modalidade.name)

    for modalidade in Modalidades:
        if (modalidade.name not in modalidade_sem_medalhas) and (modalidade.name not in modalidade_medalhas) and (modalidade.name not in modalidade_nao_participou):
            modalidade_nao_participou.append(modalidade.name)

    participou = len(modalidade_medalhas) + len(modalidade_sem_medalhas)
    nao_participou = len(modalidade_nao_participou)

    return modalidade_medalhas, modalidade_sem_medalhas, modalidade_nao_participou, participou, nao_participou

def printar_participacao(modalidade_medalhas, modalidade_sem_medalhas, modalidade_nao_participou, participou, nao_participou):
    titulo = ' PARTICIPAÇÃO E DESEMPENHO DO BRASIL '
    print(titulo.center(50, '='))
    print(f'O Brasil participou de {participou} modalidades.')
    print('='*50)

    if modalidade_medalhas:
        print('Ganhou medalhas nas seguintes modalidades: ')
        for modalidade in modalidade_medalhas:
            if modalidade_medalhas:
                print(modalidade.capitalize().replace("_", " "))
                sleep(0.2)

    else:
        print('O Brasil não ganhou medalhas.')
    if modalidade_sem_medalhas:
        print('=' * 50)
        print('Participou e não ganhou medalhas nas seguintes modalidades: ')
        for modalidade in modalidade_sem_medalhas:
            print(modalidade.capitalize().replace("_", " "))
            sleep(0.2)

    print('=' * 50)
    print(f'E por fim, não participou de {nao_participou} modalidades:')
    for modalidade in modalidade_nao_participou:
        print(modalidade.capitalize().replace("_", " "))
        sleep(0.2)

def menu(dicio_atletas, atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid):
    titulo = ' MENU DE OPÇÕES '
    print(titulo.center(40, '='))
    acao = input('Selecione a opção desejada:\n1- Mostrar opções de Modalidade\n2- Cadastrar atleta\n'
                 '3- Alterar cadastro\n4- Excluir cadastro\n5- Mostrar relatório\n6- Sair\n')
    while acao not in '123456' or acao == '':
        acao = input('\nOPÇÃO INVÁLIDA!\nSelecione a opção desejada: \n1- Mostrar opções de Modalidade\n2- Cadastrar atleta\n'
                     '3- Alterar cadastro\n4- Excluir cadastro\n5- Mostrar relatório\n6- Sair\n')
    if acao == '1':
        titulo = ' MODALIDADES '
        print(titulo.center(40, '='))
        for modalidade in Modalidades:
            print(f'{modalidade.value}- {modalidade.name.capitalize().replace("_"," ")} ')
            sleep(0.2)
        return dicio_atletas, acao

    elif acao == '2':
        dicio_atletas = ler_arquivo(dicio_atletas) #caso eu tire as funções de ler e arquivar, o arquivo só criado ao final do programa, não permitindo eu alterar ou excluir o atleta antes disso.
        cadastrar_atletas(dicio_atletas)
        arquivar_atletas(dicio_atletas)
        return dicio_atletas, acao #caso eu tire o return do dicio_atletas, recebo um erro de NULL no arquivo

    elif acao == '3':
        dicio_atletas = ler_arquivo(dicio_atletas)
        alterar_cadastro(dicio_atletas)
        arquivar_atletas(dicio_atletas)
        return dicio_atletas, acao #tentei tirar o return e o atleta não estava sendo alterado

    elif acao == '4':
        dicio_atletas = ler_arquivo(dicio_atletas)
        excluir_cadastro(dicio_atletas)
        arquivar_atletas(dicio_atletas)
        return dicio_atletas, acao

    elif acao == '5':
        if dicio_atletas != {}:
            prints_quant_atletas(atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid)
            sleep(0.3)

            matriz_medalhas, teve_medalhas = quadro_medalhas(dicio_atletas)
            sleep(0.3)

            print_quadro_medalhas(matriz_medalhas, teve_medalhas)
            sleep(0.3)

            relatorio_atleta(dicio_atletas, teve_medalhas)
            sleep(0.3)

            modalidade_medalhas, modalidade_sem_medalhas, modalidade_nao_participou, participou, nao_participou = participacao_brasil(dicio_atletas, matriz_medalhas)
            sleep(0.3)
            printar_participacao(modalidade_medalhas, modalidade_sem_medalhas, modalidade_nao_participou, participou, nao_participou)

            return dicio_atletas, acao

        else:
            print('Não há atletas cadastrados')
            return dicio_atletas, acao
    else:
        exit()
        return dicio_atletas, acao


#ARMAZENAR EM ARQUIVO
def ler_arquivo(dicio_atletas):
    if os.path.exists('cadastro_atletas.json'): #comando discutido na 3 sessão do dia 11/11/2020
        try:
            arquivo = open('cadastro_atletas.json', 'r')
            dicio_atletas = jsonpickle.decode(arquivo.read())
            arquivo.close()
        except:
            print('Não foi possível ler o arquivo.')

    return dicio_atletas


def arquivar_atletas(dicio_atletas):
    arquivo = open('cadastro_atletas.json', 'w')
    arquivo.write(jsonpickle.encode(dicio_atletas))
    arquivo.close()


def main():

    dicio_atletas = {}
    dicio_atletas = ler_arquivo(dicio_atletas)
    atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid = quantidades(dicio_atletas)
    dicio_atletas, acao = menu(dicio_atletas, atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid)
    while acao != 6:
        atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid = quantidades(dicio_atletas)
        dicio_atletas, acao = menu(dicio_atletas, atletas_fem, atletas_masc, soma_atletas, covid_fem, covid_masc, soma_covid)

        arquivar_atletas(dicio_atletas)

if __name__ == '__main__':
    main()
