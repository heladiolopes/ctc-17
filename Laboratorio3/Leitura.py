from collections import defaultdict


def Leitura(file, sep):
    f = open(file, 'r')
    lines = f.readlines()

    exemplos = []

    for l in lines:
        exemplos.append(l[:-1].split(sep))

    return exemplos


def Atributos_Exemplos():
    ages = {1: [0, 17], 18: [18, 24], 25: [25, 34], 35: [35, 44], 45: [45, 49], 50: [50, 55], 56: [56, 100]}
    occupation = {0: "other or not specified", 1: "academic/educator", 2: "artist", 3: "clerical/admin",
                  4: "college/grad student", 5: "customer service", 6: "doctor/health care", 7: "executive/managerial",
                  8: "farmer", 9: "homemaker", 10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired",
                  14: "sales/marketing", 15: "scientist", 16: "self-employed", 17: "technician/engineer",
                  18: "tradesman/craftsman", 19: "unemployed", 20: "writer"}

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
    Atributos_Exemplos()

