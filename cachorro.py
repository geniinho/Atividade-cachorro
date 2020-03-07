from random import randint

class Cachorro:
    def __init__(self, nome, raca, sexo, idade):
        self.nome = nome
        self.raca = raca
        self.sexo = sexo
        self.idade = idade
        self.energia = 100
        self.qtd_filhotes = 0

    def obter_dados(self):
        dados = f'''
Aqui estão os dados do seu pet.
Nome: {self.nome}
Raça: {self.raca}
Sexo: {self.sexo}
Idade: {self.idade}
Energia: {self.energia}
Quantidade de filhotes: {self.qtd_filhotes}'''
        return  dados

    def comer(self, comida):
        if self.energia < 50:
            if comida == 'R':
                self.energia += 50
            elif comida == 'C':
                self.energia += 40
            elif comida == 'L':
                self.energia += 30

        return self.energia

    def brincar(self, brincadeira):
        if brincadeira == 'B':
            self.energia -= 30
        elif brincadeira == 'S':
            self.energia -= 20
        elif brincadeira == 'G':
            self.energia -= 10
        return self.energia

    def pode_cruzar(self, parc):
        if (self.idade and parc.idade >= 1) and (self.idade and parc.idade <=9) and (self.raca == parc.raca) and (self.energia and parc.energia >= 80) and (self.sexo != parc.sexo):
            return True
        else:
            return False


    def cruzar(self, parc):
        if self.pode_cruzar(parc) == True:
            self.energia -= 50
            parc.energia -= 50
            filhotes = randint(3, 10)
            self.qtd_filhotes += filhotes
            parc.qtd_filhotes += filhotes
            return filhotes
        return 0