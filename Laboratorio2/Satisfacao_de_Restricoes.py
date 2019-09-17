from enum import Enum


class Cor(Enum):
    VERMELHO = 1
    AMARELO = 2
    VERDE = 3
    MARFIM = 4
    AZUL = 5


class Pais(Enum):
    INGLATERRA = 1
    ESPANHA = 2
    NORUEGA = 3
    JAPAO = 4
    UCRANIA = 5


class Cigarro(Enum):
    KOOL = 1
    LUCKY = 2
    WINSTON = 3
    PARLIAMENT = 4
    CHESTERFIELD = 5


class Bebida(Enum):
    SUCO = 1
    AGUA = 2
    CAFE = 3
    CHA = 4
    LEITE = 5


class Animal(Enum):
    ZEBRA = 1
    CAVALO = 2
    CARAMUJO = 3
    CACHORRO = 4
    RAPOSA = 5


class Value:
    def __init__(self):
        self.var = {}
        self.assigned = []
        self.unassigned = []
        for i in range(1, 6):
            self.var[Cor(i)] = -1
            self.var[Pais(i)] = -1
            self.var[Cigarro(i)] = -1
            self.var[Bebida(i)] = -1
            self.var[Animal(i)] = -1

            self.unassigned.append(Cor(i))
            self.unassigned.append(Pais(i))
            self.unassigned.append(Cigarro(i))
            self.unassigned.append(Bebida(i))
            self.unassigned.append(Animal(i))

    def check_rules(self):
        # O inglês mora na casa vermelha
        self.var[Pais.INGLATERRA] == self.var[Cor.VERMELHO]

        # O espanhol é dono do cachorro
        self.var[Pais.ESPANHA] == self.var[Animal.CACHORRO]

        # O norueguês mora na primeira casa à esquerda
        self.var[Pais.NORUEGA] == 1

        # Fumam-se cigarros Kool na casa amarela
        self.var[Cor.AMARELO] == self.var[Cigarro.KOOL]

        # O homem que fuma cigarros Chesterfield mora na casa ao lado do homem que mora com a raposa
        abs(self.var[Cigarro.CHESTERFIELD] - self.var[Animal.RAPOSA]) == 1

        # O norueguês mora ao lado da casa azul
        abs(self.var[Pais.NORUEGA] - self.var[Cor.AZUL]) == 1

        # O fumante de cigarros Winston cria caramujos
        self.var[Cigarro.WINSTON] == self.var[Animal.CARAMUJO]

        # O fumante de cigarros Lucky Strike bebe suco de laranja
        self.var[Cigarro.LUCKY] == self.var[Bebida.SUCO]

        # O ucraniano bebe chá
        self.var[Pais.UCRANIA] == self.var[Bebida.CHA]

        # O japonês fuma cigarros Parliament
        self.var[Pais.JAPAO] == self.var[Cigarro.PARLIAMENT]

        # Fumam-se cigarros Kool em uma casa ao lado da casa em que fica o cavalo
        abs(self.var[Cigarro.KOOL] - self.var[Animal.CAVALO]) == 1

        # Bebe-se café na casa verde
        self.var[Bebida.CAFE] == self.var[Cor.VERDE]

        # A casa verde está imediatamente à direita (à sua direita) da casa marfim
        self.var[Cor.VERDE] - self.var[Cor.MARFIM] == 1

        # Bebe-se leite na casa do meio
        self.var[Bebida.LEITE] == 3


class Node:
    def __init__(self):
        self.filho = []
        self.pai = None
        self.value = None


if __name__ == '__main__':
    raiz = Node()
    raiz.value = Value()
