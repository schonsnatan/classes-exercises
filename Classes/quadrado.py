'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

'''

class Quadrado:
    def __init__(self,tamanho_lado:float):
        self.tamanho = tamanho_lado

    def mudarValor(self,novo_valor):
        self.tamanho = novo_valor
        self.retornarValorLado()
        self.calcularArea()
    
    def retornarValorLado(self):
        print(f'O tamanho do lado é {self.tamanho}')

    def calcularArea(self):
        self.retornarValorLado()
        area = self.tamanho ** 2
        print(f'A area do quadrado é {area}')

quadrado1 = Quadrado(12.4)
quadrado1.retornarValorLado()
quadrado1.mudarValor(14.4)