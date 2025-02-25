import time
import calcDescontos
import sorteioNumeros
import  interface

print("================================\nBem vindo ao Sistem da nossa Loja\n================================\n")


# While principal do projeto, onde chamo os arquivos numa ordem em match case.

while True :
    print("📋 Escolha uma opção: \n ▶ 1 - Calculo de Desconto\n ▶ 2 - Sorteio de numeros\n ▶ 3 - Veja com Interface grafica\n ▶ 0 - Sair do programa 😥")
    opcao = int(input("Digite o numero da opção: "))


    #  Monatgem do menu de opções onde chamarei as funções dos modulos de acordo com a opção escolhida
    match opcao:
        case 1:
            # Chamando a função do modulo calcDescontos
            calcDescontos.calcularDesconto()
        case 2:
            # Chamando a função do Modulo de SorteioNumeros
            sorteioNumeros.sortear()
        case 3:
            interface.main()
        case 0:
            print("┎───────────────────────\n│Que triste 😥 estou encerrando o software \n│ Caso queira continuar precione 0 novamente \n┕───────────────\n")

            porc = 0
            while porc < 110:
                print(porc , "%", end=' | ')
                time.sleep(1)
                porc = porc + 10
            break
        case _:
            print("\n┎───────────────────────\n❌ OPÇÃO INVALIDA - tente novamente ou digite 0 para sair\n┕───────────────\n")