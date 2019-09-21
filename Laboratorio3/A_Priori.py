from Leitura import Leitura
from Split import split_train_test


def a_priori_examples():
    ratings = Leitura('ml-1m/ratings.dat', '::')
    examples = []

    for i in range(len(ratings)):
        movie_id = ratings[i][1]
        rating = ratings[i][2]
        examples.append([movie_id, rating])

    return examples


def a_priori_train_test(examples):
    percent = 0.6
    train, test = split_train_test(examples, percent)

    return train, test


def a_priori_median_ratings(train):
    moviesRatingsDict = {}
    all_ratings = []

    for i in range(len(train)):
        movie_id = train[i][0]
        rating = train[i][1]

        if movie_id in moviesRatingsDict:
            moviesRatingsDict[movie_id].append(rating)
        else:
            moviesRatingsDict[movie_id] = [rating]
        all_ratings.append(rating)

    for key in moviesRatingsDict:
        moviesRatingsDict[key].sort()
        moviesRatingsDict[key] = moviesRatingsDict[key][len(moviesRatingsDict[key])//2]
        #print(key, moviesRatingsDict[key])
    all_ratings.sort()
    all_ratings = all_ratings[len(all_ratings)//2]

    #print(moviesRatingsDict, all_ratings)

    return moviesRatingsDict, all_ratings


if __name__ == "__main__":
    examples = a_priori_examples()
    train, test = a_priori_train_test(examples)
    moviesRatingsDict, all_ratings = a_priori_median_ratings(train)

