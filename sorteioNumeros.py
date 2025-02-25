import random

# Aqui criamos uma função para sortear, para depois chamar no arquivo principal...
def sortear():
    print("\n   ➥ MODULO - SORTEIO DE NUMERO \n")
    qtdNumeros = int(input("        ▶ Informe até qual numero deseja que seja sorteado: "))


    sortearNumero = random.randrange(0, qtdNumeros)

    print("┎───────────────────────\n│🎉 O numero sorteado foi :", sortearNumero,   "\n│ Parabéns  o numero ", sortearNumero ," é o ganhador(a) \n┕───────────────\n")


# Função que retorna a string para a interface
def sortear2(numero):
    qtdNumeros = int(numero)
    sortearNumero = random.randrange(0, qtdNumeros)

    retorno = "┎───────────────────────\n│🎉 O numero sorteado foi : {} \n│ Parabéns  o numero {}  é o ganhador(a) \n┕───────────────\n".format(sortearNumero, sortearNumero)
    return retorno