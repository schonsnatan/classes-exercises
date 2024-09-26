'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self,nome: str,idade: int,peso: float,altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def exibir_status(self):
        '''Exibe o status atual da pessoa.'''
        print(f'Nome: {self.nome}, Idade: {self.idade} anos, Altura: {self.altura} cm, Peso: {self.peso} kg.')

    def crescer(self,crescimento: float):
        '''Aumenta a altura da pessoa se houver crescimento.'''
        if crescimento > 0:
            print(f'\nCRESCER: {self.nome} cresceu {crescimento} cm.')
            self.altura += crescimento
        self.exibir_status()

    def engordar(self, peso_ganho: float):
        '''Aumenta o peso da pessoa'''
        print(f'\nENGORDAR:{self.nome} ganhou {peso_ganho} kg.')
        self.peso += peso_ganho
        self.exibir_status()

    def emagrecer(self, peso_perdido: float):
        '''Reduz o peso da pessoa'''
        print(f'\nEMAGRECER: {self.nome} perdeu {peso_perdido} kg.')
        self.peso -= peso_perdido
        if self.peso < 0:
            self.peso = 0 #Evita peso negativo
        self.exibir_status()

    def envelhecer(self,anos):
        print(f'\nENVELHECER: {self.nome} envelheceu {anos} anos.')
        crescimento=0
        for ano in range(anos):
            self.idade+=1
            if self.idade <= 21:
                crescimento+=0.5
        self.exibir_status()
        if crescimento > 0:
            self.crescer(crescimento)

def main():      
    pessoa1 = Pessoa('Natan',15,80.5,187)
    pessoa1.crescer(5)

if __name__ == "__main__":
    main()