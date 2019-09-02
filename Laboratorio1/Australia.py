import pandas as pd
from math import sqrt, inf
from datetime import datetime as dt


class City:
    def __init__(self, id, name, lat, lng, stt, pop, ngb):
        self.id = id
        self.name = name
        self.lat = lat
        self.lng = lng
        self.state = stt
        self.population = pop
        self.neighbor = ngb
        self.parent = -1

    def __str__(self):
        return 'id:{:3}|name:{:20}|ngb:{}'.format(self.id, self.name, self.neighbor)


class Country:
    def __init__(self, file):
        city = pd.read_csv(file)  # Reading file with data
        self.cities = [None]  # Cities vector

        for i in range(city.shape[0]):
            ct = City(city.loc[i]['id'], city.loc[i]['city'], city.loc[i]['lat'],
                      city.loc[i]['lng'], city.loc[i]['state/territory'], city.loc[i]['population'],
                      self.neighbor(city.loc[i]['id'], city.shape[0]))
            self.cities.append(ct)

        self.bidirecional()

    def path(self, start, end, method):

        if type(start) == str:
            aux = 1
            while self.cities[aux].name != start:
                aux = aux + 1
            start = aux
        if type(end) == str:
            aux = 1
            while self.cities[aux].name != end:
                aux = aux + 1
            end = aux

        # Reset parent status
        for i in range(1, len(self.cities)):
            self.cities[i].parent = -1

        # Do selected method
        time = 0
        if method == 'greedy':
            time = dt.now()
            self.__greedy(start, end)
            time = dt.now() - time
        elif method == 'A*':
            time = dt.now()
            self.__star_A(start, end)
            time = dt.now() - time

        # Getting path
        stack = [end]
        while self.cities[stack[len(stack) - 1]].id != start:
            stack.append(self.cities[stack[len(stack) - 1]].parent)
        path = stack[::-1]

        # Distance
        d = 0
        for i in range(1, len(path)):
            d += 1.1 * self.distance(self.cities[path[i - 1]], self.cities[path[i]])

        # Print details
        print('\n{} METHOD'.format(method.upper()))
        print('Path from {} to {} by id:'.format(self.cities[start].name, self.cities[end].name))
        print(path)
        print('Distance by {} method: {:.2f}'.format(method, d))
        print('Steps: {} '.format(len(path)-1))
        print('Time: {} s\n'.format(time))

    def __greedy(self, start, end):
        # Start g and f cost for all nodes
        g = [inf] * len(self.cities)
        f = [inf] * len(self.cities)
        # Everyone is open
        closed = [False] * len(self.cities)

        pq = []  # Priority queue

        g[start] = 0
        f[start] = self.distance(self.cities[start], self.cities[end])

        pq.append((f[start], start))

        while len(pq) > 0:
            # Extract min from pq
            pq.sort(key=lambda tup: tup[0], reverse=True)
            node = pq.pop()

            if not closed[node[1]]:
                closed[node[1]] = True

                for successor in self.cities[node[1]].neighbor:

                    cost_node_successor = self.distance(self.cities[node[1]], self.cities[successor])
                    cost_successor_end = self.distance(self.cities[successor], self.cities[end])

                    if not closed[successor]:
                        self.cities[successor].parent = node[1]
                        g[successor] = g[node[1]] + cost_node_successor
                        f[successor] = cost_successor_end

                        if successor == end:
                            return

                        pq.append((f[successor], successor))

    def __star_A(self, start, end):
        # Start g and f cost for all nodes
        g = [inf]*(len(self.cities))
        f = [inf]*(len(self.cities))
        # Everyone is open
        closed = [False] * len(self.cities)

        pq = []  # Priority queue

        g[start] = 0
        f[start] = self.distance(self.cities[start], self.cities[end])

        pq.append((f[start], start))

        while len(pq) > 0:
            # Extract min from pq
            pq.sort(key=lambda tup: tup[0], reverse=True)
            node = pq.pop()

            if not closed[node[1]]:
                closed[node[1]] = True

                if node[1] == end:
                    return

                for successor in self.cities[node[1]].neighbor:

                    cost_node_successor = self.distance(self.cities[node[1]], self.cities[successor])
                    cost_successor_end = self.distance(self.cities[successor], self.cities[end])

                    if not closed[successor] and f[successor] > g[node[1]] + cost_node_successor + cost_successor_end:
                        g[successor] = g[node[1]] + cost_node_successor
                        f[successor] = g[successor] + cost_successor_end

                        self.cities[successor].parent = node[1]
                        pq.append((f[successor], successor))

    @staticmethod
    def neighbor(x, max):
        """
        :param x: id from city
        :param max: cities per country
        :return: neighbor from city x
        """
        ngb = []
        if x % 2 == 0:
            if x > 1:
                ngb.append(x - 1)
            if x < max-1:
                ngb.append(x + 2)
        elif x % 2 == 1:
            if x > 2:
                ngb.append(x - 2)
            if x < max:
                ngb.append(x + 1)
        return ngb

    @staticmethod
    def distance(city_1, city_2):
        """
        Real distance between two cities
        :param city_1: object city 1
        :param city_2: object city 2
        :return: euclidean distance
        """
        return sqrt((city_1.lat - city_2.lat) ** 2 + (city_1.lng - city_2.lng) ** 2)

    def bidirecional(self):
        for i in range(1, len(self.cities)):
            for ngb in self.cities[i].neighbor:
                if i not in self.cities[ngb].neighbor:
                    self.cities[ngb].neighbor.append(i)
            self.cities[i].neighbor.sort()


if __name__ == '__main__':
    ct = Country('australia.csv')

    start = 'Alice Springs'
    end = 'Yulara'

    ct.path(start, end, 'greedy')
    ct.path(start, end, 'A*')

    # for x in range(1, len(ct.cities)):
        # print('d:{:20} - x:{:3}'.format(Country.distance(ct.cities[x], ct.cities[219]), x), ct.cities[x])
        # print('x:{:3}'.format(x), ct.cities[x], '|parent: {}'.format(ct.cities[x].parent))
        # print('x:{:3}'.format(x), ct.cities[x])
