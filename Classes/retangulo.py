'''
Classe Retangulo: Crie uma classe que modele um retangulo:

a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para
o local.

'''

class Retangulo:
    def __init__(self,base:float, altura: float):
        self.base = base
        self.altura = altura
    
    def mudarValorLado(self):
        lado = 5
        while lado!=0:
            lado = int(input(''' [1] para mudar base\n [2] para mudar altura\n [3] para mudar ambos:\n [0] para sair: '''))
            if lado == 3:
                valor_base = float(input('Digite o valor da base: '))
                valor_altura = float(input('Digite o valor da altura: '))
                self.base = valor_base
                self.altura = valor_altura
            elif lado == 1:
                valor_mudado = float(input('Digite o valor da base a ser alterado: '))
                self.base = valor_mudado
            elif lado == 2:
                valor_mudado = float(input('Digite o valor da altura a ser alterado: '))
                self.altura = valor_mudado
            elif lado==0:
                print('Saindo...')
            else: 
                print('Digite um valor válido')
        self.retornarValorLados()

    def retornarValorLados(self):
        print(f'A altura tem valor {self.altura} e a base tem valor {self.base}')

    def calcularArea(self) -> float:
        area = self.base * self.altura
        print(f'A área do retangulo é de {area}')
        return area

    def calcularPerimetro(self) -> float:
        perimetro = 2*(self.base + self.altura)
        print(f'O perímetro do retângulo é de {perimetro}')
        return perimetro
    
    def calcularPisoseRodapes(self, tamanho_piso: float, tamanho_rodape: float):
        area_local = self.calcularArea()
        perimetro_local = self.calcularPerimetro()

        quantidade_pisos = area_local / tamanho_piso
        quantidade_rodape = perimetro_local / tamanho_rodape

        print(f'Você precisa de {quantidade_pisos:.2f} pisos.')
        print(f'Você precisa de {quantidade_rodape:.2f} rodapes.')

def main():
    altura = 5.0
    base = 4.0  
    tamanho_piso = 1.0 #nesse caso o piso tem 1 m2
    tamanho_rodape = 0.5 #nesse caso o piso tem 0.5 metros  

    retangulo1 = Retangulo(base,altura)
    retangulo1.mudarValorLado()
    retangulo1.calcularPisoseRodapes(tamanho_piso,tamanho_rodape)

if __name__ == "__main__":
    main()

 