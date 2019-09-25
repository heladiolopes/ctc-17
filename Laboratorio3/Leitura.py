from collections import defaultdict


def Leitura(file, sep):
    f = open(file, 'r', encoding="ISO-8859-1")
    lines = f.readlines()

    exemplos = []

    for l in lines:
        exemplos.append(l[:-1].split(sep))

    return exemplos


def Atributos_Exemplos():
    ratings = Leitura('ml-1m/ratings.dat', '::')

    users = Leitura('ml-1m/users.dat', '::')
    usersDict = {}
    for i in range(len(users)):
        usersDict[users[i][0]] = users[i][1:4]

    movies = Leitura('ml-1m/movies.dat', '::')
    moviesDict = {}
    for i in range(len(movies)):
        aux = movies[i][2]
        aux = aux.split("|")
        moviesDict[movies[i][0]] = aux

    genres = []
    for i in range(len(movies)):
        genre = movies[i][2]
        genre = genre.split("|")
        for j in range(len(genre)):
            if genre[j] not in genres:
                genres.append(genre[j])
    genres.sort()

    examples = [[""]*(3 + len(genres) + 1) for i in range(len(ratings))]

    for i in range(len(ratings)):
        user_id = ratings[i][0]
        movie_id = ratings[i][1]
        rating = ratings[i][2]

        for j in range(3):
            examples[i][j] = usersDict[user_id][j]

        for j in range(len(genres)):
            if genres[j] in moviesDict[movie_id]:
                examples[i][j+3] = "SIM"
            else:
                examples[i][j+3] = "NAO"

        examples[i][-1] = rating

    attributes = defaultdict(list)
    for i in range(len(users)):
        for k in range(1, 4):
            if users[i][k] not in attributes[k-1]:
                attributes[k-1].append(users[i][k])
    attributes[0].sort()
    attributes[1].sort()
    attributes[2].sort()
    for i in range(18):
        attributes[i+3] = ["NAO", "SIM"]

    print("OK")

    return examples, attributes


if __name__ == '__main__':
    ex, at = Atributos_Exemplos()
    # for l in ex:
    #     print(l)
    print(list(at.keys())[0])
