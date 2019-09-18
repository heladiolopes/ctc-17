from Arvore import Aprendizado, Maioria, MostraArvore, Classificar
# from Leitura import Leitura


attributes = {0: ["Ensolarado", "Nublado", "Chuvoso"], 1: ["Quente", "Boa", "Fria"],
              2: ["Alta", "Normal"], 3: ["Forte", "Fraco"]}

examples = [["Ensolarado", "Quente", "Alta", "Fraco", "NAO"],
                ["Ensolarado", "Quente", "Alta", "Forte", "NAO"],
                ["Nublado", "Quente", "Alta", "Fraco", "SIM"],
                ["Chuvoso", "Boa", "Alta", "Fraco", "SIM"],
                ["Chuvoso", "Fria", "Normal", "Fraco", "SIM"],
                ["Chuvoso", "Fria", "Normal", "Forte", "NAO"],
                ["Nublado", "Fria", "Normal", "Forte", "SIM"],
                ["Ensolarado", "Boa", "Alta", "Fraco", "NAO"],
                ["Ensolarado", "Fria", "Normal", "Fraco", "SIM"],
                ["Chuvoso", "Boa", "Normal", "Fraco", "SIM"],
                ["Ensolarado", "Boa", "Normal", "Forte", "SIM"],
                ["Nublado", "Boa", "Alta", "Forte", "SIM"],
                ["Nublado", "Quente", "Normal", "Fraco", "SIM"],
                ["Chuvoso", "Boa", "Alta", "Forte", "NAO"]]


arvore = Aprendizado(examples, attributes, Maioria(examples))

MostraArvore(arvore)

print('\n')

print(Classificar(arvore, ["Ensolarado", "Fria", "Alta", "Forte"]))
