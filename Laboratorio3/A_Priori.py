from Leitura import Leitura
from Split import split_train_test
from collections import defaultdict


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


def separate_groups(ratings):
    groups = defaultdict(int)

    for i in range(len(ratings)):
        groups[ratings[i]] += 1

    return groups


def most_common(groups):
    most_common_number = -1
    most_common_value = -1

    for value in groups:
        if groups[value] > most_common_number:
            most_common_number = groups[value]
            most_common_value = value

    return most_common_value


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
        groups = separate_groups(moviesRatingsDict[key])
        mode = most_common(groups)
        moviesRatingsDict[key] = mode
    all_groups = separate_groups(all_ratings)
    all_mode = most_common(all_groups)
    all_ratings = all_mode

    #print(moviesRatingsDict, all_ratings)

    return moviesRatingsDict, all_ratings


def a_priori_rating(test, moviesRatingsDict, all_ratings):
    test_rating = []

    for i in range(len(test)):
        movie_id = test[i][0]

        if movie_id in moviesRatingsDict:
            test_rating.append([movie_id, moviesRatingsDict[movie_id]])
        else:
            test_rating.append([movie_id, all_ratings])

    return test_rating


if __name__ == "__main__":
    examples = a_priori_examples()
    train, test = a_priori_train_test(examples)
    moviesRatingsDict, all_ratings = a_priori_median_ratings(train)
    test_rating = a_priori_rating(test, moviesRatingsDict, all_ratings)

    #for i in range(len(test)):
    #    print(test[i][1], test_rating[i][1])

