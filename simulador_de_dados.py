# simulador de dado
# simular o uso de um dadao gerando um valor de 1 ate 6
import random


class SimuladorDeDado:
    def __init__(self):
        self.Valor_minimo = 1
        self.Valor_maximo = 6
        self.mensagem = 'voce gostaria de gerar um novo valor para o dado ?'

    def Inicar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.ValorDoDado()
        elif resposta == 'nao' or resposta == 'n':
            print('agradecemos sua participacao')
        else:
            print('favor inserir sim ou nao')

    def ValorDoDado(self):
        print(random.randint(self.Valor_minimo, self.Valor_maximo))


simulador = SimuladorDeDado()
simulador.Inicar()
