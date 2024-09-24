'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

'''

class Bola:
    def __init__(self,cor: str,circunferencia: float,material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        self.mostraCor()

    def mostraCor(self) -> None:
        print(f'A Bola é de cor {self.cor}, tem uma circunferencia de {self.circunferencia} e material {self.material}')

bola_azul = Bola('azul',35,'plástico')
bola_azul.mostraCor()
bola_azul.trocaCor('vermelha')