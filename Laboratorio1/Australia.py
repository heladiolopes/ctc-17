import pandas as pd


class City:
    def __init__(self, id, name, lat, lng, stt, pop, ngb):
        self.id = id
        self.name = name
        self.lat = lat
        self.lng = lng
        self.state = stt
        self.population = pop
        self.neighbor = ngb


class Country:
    def __init__(self, file):
        self.city = pd.read_csv(file)
        self.cities = [None]

        for i in range(self.city.shape[0]):
            x = self.city.loc[i]['id']
            print('id: {:3}| neighbor: {}'.format(x, self.neighbor(x)))

        for i in range(self.city.shape[0]):
            ct = City(self.city.loc[i]['id'], self.city.loc[i]['city'], self.city.loc[i]['lat'],
                      self.city.loc[i]['lng'], self.city.loc[i]['state/territory'], self.city.loc[i]['population'],
                      self.neighbor(self.city.loc[i]['id']))
            self.cities.append(ct)

    def path(self, init, end, method):
        pass

    def greedy(self):
        pass

    def star_A(self):
        pass

    def neighbor(self, x):
        ngb = []
        if x % 2 == 0:
            if x > 1:
                ngb.append(x - 1)
            if x < self.city.shape[0]-2:
                ngb.append(x + 2)
        elif x % 2 == 1:
            if x > 2:
                ngb.append(x - 2)
            if x < self.city.shape[0]-1:
                ngb.append(x + 1)

        return ngb


if __name__ == '__main__':
    ct = Country('australia.csv')

    for x in range(1,len(ct.cities)):
        print('x: {:3}|id: {:3}, name: {:15}|neigbor: {}'.format(x, ct.cities[x].id, ct.cities[x].name, ct.cities[x].neighbor))
