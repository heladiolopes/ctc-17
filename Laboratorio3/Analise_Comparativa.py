class Analise:
    def __init__(self, correto, predito, classes):
        assert len(correto) == len(predito), "Comprimento incompatível dos vetores."
        self.c = correto
        self.p = predito
        self.n = len(correto)

        self.classe = classes

    # Taxa de acerto
    def taxa_acerto(self):
        acerto = 0
        for i in range(self.n):
            if self.c[i] == self.p[i]:
                acerto += 1
        return acerto/self.n

    # Matriz de confusão
    def matriz_confusao(self):
        x = self.classe
        matriz = []
        for i in range(x):
            matriz.append([])
            for k in range(x):
                matriz[i].append(0)

        for i in range(self.n):
            matriz[self.c[i]-1][self.p[i]-1] += 1
        return matriz

    # Erro quadrático médio
    def erro_quad_med(self):
        erro = 0
        for i in range(self.n):
            erro += (self.c[i] - self.p[i])**2
        return erro/self.n

    # Estatística kappa
    def kappa(self):
        p = []
        c = []
        for i in range(self.classe):
            p.append(0)
            c.append(0)
            for k in range(self.n):
                if self.p[k] == i+1:
                    p[i] += 1
                if self.c[k] == i+1:
                    c[i] += 1

        po = self.taxa_acerto()
        pe = 0
        for i in range(self.classe):
            pe += p[i]*c[i]
        pe /= (self.n**2)

        return (po-pe)/(1-pe)

    # Estatistica geral
    def estatisticas(self):
        print('ESTATÍSTICAS DA CLASSIFICAÇÃO:')
        print('\nTaxa de acerto: {}'.format(self.taxa_acerto()))
        print('\nMatriz de confusão: ')
        matriz = self.matriz_confusao()

        print('\t\t', end='')
        for i in range(self.classe):
            print('  [{}]  '.format(i+1), end='', sep='')
        print()

        for i in range(self.classe):
            print('[{}] -> '.format(i+1), end='', sep='')
            for elemento in matriz[i]:
                print('| {:4} '.format(elemento), end='', sep='')
            print('|')

        print('\nErro quadrático médio:', self.erro_quad_med())

        print('\nKappa:', self.kappa())


if __name__ == '__main__':
    correct = [1, 2, 3, 4, 4, 2, 2, 4, 5, 2, 2, 4, 2, 5]*13
    # predict = [1, 3, 3, 4, 4, 2, 2, 4, 5, 2, 2, 4, 2, 5]
    predict = [1, 2, 3, 4, 5, 1, 2, 4, 5, 4, 2, 4, 1, 3]*13

    analise = Analise(correct, predict, 5)

    analise.estatisticas()
