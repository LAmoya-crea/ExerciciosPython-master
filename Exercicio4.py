class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5

Lucas = Pessoa(nome = 'Lucas', idade = 10, peso = 70.0, altura = 1.78)
print(f'Nome: {Lucas.nome}, Idade: {Lucas.idade}, Peso: {Lucas.peso}, Altura: {Lucas.altura}')
while Lucas.idade < 80:
    Lucas.envelhecer()
    Lucas.engordar()
   Lucas.emagrecer()
    Lucas.crescer()
    print(f'Nome: {Lucas.nome}, Idade: {Lucas.idade}, Peso: {Lucas.peso}, Altura: {round(Lucas.altura,2)}')


