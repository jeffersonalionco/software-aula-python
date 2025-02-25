import random

#função principal do codigo
def calcularDesconto():

    # Aqui geramos um numero aleatorio
    # numero_aleatorio = random.randrange(0, 40)


    print("\n   ➥ MODULO - CALCULO DE DESCONTO \n")
    preco = float(input("       Digite o preço do produto? "))
    porcentagem = float(input("       Digite a porcentagem de desconto:  "))

    result = (preco * porcentagem) / 100

    print("┎───────────────────────\n│Você ganhou R$", round(result, 2) , " de Desconto! \n│Valor total final: R$ ", round(preco - result, 2), "\n┕───────────────\n")




# função principal do codigo
def calcularDesconto2(valor):


    # Aqui geramos um numero aleatorio
    numero_aleatorio = random.randrange(0, 40)


    preco = float(valor)

    result = (preco * numero_aleatorio) / 100
    retorno = "┎───────────────────────\n│Você ganhou R$ {} de Desconto! \n│Valor total final: R$ {} \n┕───────────────\n".format(round(result,2), round(
        preco - result, 2))

    return  retorno