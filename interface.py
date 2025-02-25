import tkinter as tk
import calcDescontos
import sorteioNumeros

def main():
    janela = tk.Tk()

    janela.title("Bem vindo ao meu Programa")
    janela.geometry("400x200")





    # Criei a janela de descontos quando o usuario solicitar
    def interfaceDescontos():
        """DEFININDO TAMANHO DA JANELA DE DESCONTOS"""
        descontos = tk.Tk()
        descontos.title("Janela para calculo de descontos")
        descontos.geometry("600x250")

        """Criando titulo de exibição solicitando um valor"""
        label = tk.Label(descontos, text="Digite o valor do Produto: ", font=("Arial", 12))
        label.grid(row = 0, column= 0, padx=10, pady=15)

        """Campo de imput para pegar o valor do produto"""
        entradaValor = tk.Entry(descontos)
        entradaValor.grid(row = 0, column= 1, padx=10, pady=30)

        # Função que exibi o resultado do valor que o usuario digita no campo com descontos
        def exibirDados():
            retorno = calcDescontos.calcularDesconto2(entradaValor.get())
            label1 = tk.Label(descontos, text=retorno, font=("Arial", 12), anchor="w", justify="left")
            label1.grid(row = 1, column= 0, padx=0, pady=0)

        confirmar = tk.Button(descontos, text="Confirmar", command=exibirDados)
        confirmar.grid(row = 0, column= 3, padx=0, pady=30)





#Criando a Janela de sorteio
    def sortearNumero():
        """ Definindo o titulo e o tamanho da tela de sorteios"""
        sorteio = tk.Tk()
        sorteio.title("Bem Vido a aba de sorteios")
        sorteio.geometry("600x250")

        """Solicitar até qual numero deseja sortear"""
        info = tk.Label(sorteio, text="Informe até qual numero deseja sortear", font=("Arial", 12))
        info.grid(row=0, column=0, padx=10, pady=10)

        """Campo para o usuario informar o valor"""
        entrada = tk.Entry(sorteio)
        entrada.grid(row=0, column=1, padx=10, pady=10)

        def gerarNumero():
            texto = sorteioNumeros.sortear2(entrada.get())

            info = tk.Label(sorteio, text=texto, font=("Arial", 12),  anchor="w", justify="left")
            info.grid(row=1, column=0, padx=10, pady=10)

        confirmar = tk.Button(sorteio, text="Gerar Numero", command=gerarNumero)
        confirmar.grid(row=0, column=2, padx=10, pady=10)


        #lABEL E BOTEOES DA INTERFACE PRINCIPAL
    label = tk.Label(janela, text="Estas são algumas das funções do nosso sistema\n\n", font=("Arial", 12))
    label.grid(row=0, column=0, padx=10, pady=0)
    botao = tk.Button(janela, text="MODULO - CALCULO DE DESCONTOS", command=interfaceDescontos, bg="#836FFF", fg="white")
    botao.grid(row=1, column=0, sticky= "ew",  padx=5, pady=5)
    botao = tk.Button(janela, text="MODULO - SORTEIO DE NUMEROS", command=sortearNumero, bg="#836FFF", fg="white")
    botao.grid(row=2, column=0, sticky= "ew", padx=5, pady=5)


    #INICIA O PROCESSO DE LOOP DA INTERFACE PRINCIPAL.
    janela.mainloop()