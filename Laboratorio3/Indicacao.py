from Arvore import Aprendizado, Maioria, MostraArvore, Classificar
from Leitura import Atributos_Exemplos, Leitura
from Split import split_train_test


def user_info():
    ages = {1: [0, 17], 18: [18, 24], 25: [25, 34], 35: [35, 44], 45: [45, 49], 50: [50, 55], 56: [56, 100]}
    occupations = {0: "other or not specified", 1: "academic/educator", 2: "artist", 3: "clerical/admin",
                  4: "college/grad student", 5: "customer service", 6: "doctor/health care", 7: "executive/managerial",
                  8: "farmer", 9: "homemaker", 10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired",
                  14: "sales/marketing", 15: "scientist", 16: "self-employed", 17: "technician/engineer",
                  18: "tradesman/craftsman", 19: "unemployed", 20: "writer"}

    print("Digite o genero (M/F)!")
    # genre = input()
    genre = "M"

    print("Digite a idade (0-100)!")
    # age = input()
    age = 32

    for key in ages:
        if ages[key][0] <= age <= ages[key][1]:
            age = str(key)
            break

    print("Digite a profissao!")
    # occupation = input()
    occupation = "farmer"

    for key in occupations:
        if occupation == occupations[key]:
            occupation = str(key)
            break

    return genre, age, occupation


def create_examples(p_genre, age, occupation):
    movies = Leitura('ml-1m/movies.dat', '::')
    for i in range(len(movies)):
        aux = movies[i][2]
        aux = aux.split("|")
        movies[i][2] = aux

    genres = []
    for i in range(len(movies)):
        genre = movies[i][2]
        for j in range(len(genre)):
            if genre[j] not in genres:
                genres.append(genre[j])
    genres.sort()

    examples = [[""] * (3 + len(genres) + 1 + 1) for i in range(len(movies))]

    for i in range(len(movies)):
        examples[i][0] = p_genre
        examples[i][1] = age
        examples[i][2] = occupation
        
        movie_id = movies[i][0]
        movie_title = movies[i][1]
        movie_genres = movies[i][2]

        for j in range(len(genres)):
            if genres[j] in movie_genres:
                examples[i][j+3] = "SIM"
            else:
                examples[i][j+3] = "NAO"

        examples[i][-2] = movie_title
        examples[i][-1] = "0"

    return examples


def rate_movies(examples):
    train, attributes = Atributos_Exemplos()
    train, _ = split_train_test(train, 0.7)
    test = examples

    # print(len(train), len(train[0]))
    # print(train[0])
    # print(len(test), len(test[0]))
    # print(test[0])

    arvore = Aprendizado(train, attributes, Maioria(train))

    # print('Aprendido')
    ratings = []
    for line in test:
        ratings.append((line[-2], int(Classificar(arvore, line))))
        # line[-1] = a

    return ratings
    # print(test)


if __name__ == "__main__":
    genre, age, occupation = user_info()
    examples = create_examples(genre, age, occupation)
    ratings = rate_movies(examples)

    ratings.sort(key=lambda x: x[1], reverse=True)
    n = input('Quantas recomendações você deseja: ')
    for i in range(n):
        print('{:2}: {:50} -> {}'.format(i+1, ratings[i][0], ratings[i][1]))
