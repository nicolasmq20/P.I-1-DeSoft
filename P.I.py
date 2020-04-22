########################################################################################################################
########################################----Autor: Davi Reis Vieira de Souza----########################################
################################################----P.I nº1 DeSoft----##################################################
########################################################################################################################

###################################################----QUESTÃO 1-----###################################################

valor_salario = float(input("Qual o valor de seu salário bruto?"))
numero_dependentes = float(input("Quantos dependentes você possui?"))


def contribuicao_inss(salariobruto):
    if salariobruto <= 1045.00:
        return salariobruto*0.075
    elif salariobruto >= 1045.01 and salariobruto <= 2089.60:
        return salariobruto*0.09
    elif salariobruto >= 2089.61 and salariobruto <= 3134.40:
        return salariobruto*0.12
    elif salariobruto >= 3134.41 and salariobruto <= 6101.06:
        return salariobruto*0.14
    else:
        return 671.12


def base_calculo(salariobruto, contribuicao, dependentes):
    return salariobruto-contribuicao-dependentes*189.59


def aliquota_deducao(base_calculo):
    if base_calculo <= 1903.98:
        return 0, 0
    elif base_calculo >= 1903.99 and base_calculo <= 2826.65:
        return 0.075, 142.80
    elif base_calculo >= 2826.66 and base_calculo <= 3751.05:
        return 0.15, 354.80
    elif base_calculo >= 3751.06 and base_calculo <= 4664.68:
        return 0.225, 636.13
    else:
        return 0.275, 869.36


base_calculo_valor = base_calculo(
    valor_salario, contribuicao_inss(valor_salario), numero_dependentes)
aliquota_deducao_valor = aliquota_deducao(base_calculo_valor)

irrf = base_calculo_valor*aliquota_deducao_valor[0] - aliquota_deducao_valor[1]
print(irrf)

###################################################----QUESTÃO 2-----###################################################


def calcula_pi(n):
    somatorio = 0
    for i in range(n+1):
        if i == 0:
            somatorio += 0
        else:
            somatorio += 6/(i**2)
    return somatorio**(1/2)


print(calcula_pi(5))
###################################################----QUESTÃO 3-----###################################################


test_list = [1, 4, 5, 7, 8, 10]
test_list = [4, 3, 2, 1]
test_list = [4, 3]


def estritamente_crescente(list):
    return all(a < b for a, b in zip(list, list[1:]))


def estritamente_decrescente(list):
    return all(a > b for a, b in zip(list, list[1:]))


def classifica_lista(list):
    if len(list) >= 2:
        if estritamente_crescente(list):
            return 'crescente'
        elif estritamente_decrescente(list):
            return 'decrescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'


print(classifica_lista(test_list))

###################################################----QUESTÃO 4-----###################################################


def verifica_preco(livro, nomelivros, dicionarioprecos):
    if livro in nomelivros:
        cor = nomelivros[livro]
        if cor in dicionarioprecos:
            valor = dicionarioprecos[cor]
            return valor


livro = "Dom Quixote"
nomelivros = {"Pinóquio": "azul", "Dom Quixote": "amarelo",
              "O Pequeno Príncipe": "vermelho"}
dicionarioprecos = {"vermelho": 10.0,
                    "azul": 20.0, "amarelo": 40.0, "verde": 100.0}

print(verifica_preco(livro, nomelivros, dicionarioprecos))

###################################################----QUESTÃO 5-----###################################################

dicionario = {'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}


def agrupa_por_idade(dicionario):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    faixaetaria = dict()
    for k, v in dicionario.items():
        if v <= 11:
            criança.append(k)
        elif v >= 12 and v <= 17:
            adolescente.append(k)
        elif v >= 18 and v <= 59:
            adulto.append(k)
        else:
            idoso.append(k)
    faixaetaria['criança'] = criança
    faixaetaria['adolescente'] = adolescente
    faixaetaria['adulto'] = adulto
    faixaetaria['idoso'] = idoso
    return faixaetaria


print(agrupa_por_idade(dicionario))
