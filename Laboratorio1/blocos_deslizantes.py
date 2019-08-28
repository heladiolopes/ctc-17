#import heapq
from math import inf


class Node:
    def __init__(self, value):
        self.value = value
        self.closed = False
        self.g = inf
        self.f = inf


class Box:
    def __init__(self, boxes):
        self.boxes = boxes

        self.x_0 = -1
        self.y_0 = -1

        self.coord = {}
        self.movements = []
        self.distance = 0

        self.zero()
        self.coordinates()

    def zero(self):
        for i in range(len(self.boxes)):
            for k in range(len(self.boxes[0])):
                if self.boxes[i][k] == 0:
                    self.x_0 = i
                    self.y_0 = k
                    break

    def coordinates(self):
        for i in range(len(self.boxes)):
            for k in range(len(self.boxes[0])):
                self.coord[self.boxes[i][k]] = [i, k]

    def neighbors(self):
        changed = [[0]*len(self.boxes[0]) for i in range(len(self.boxes))]
        for i in range(len(self.boxes)):
            for k in range(len(self.boxes[0])):
                changed[i][k] = self.boxes[i][k]

        self.movements = []
        if self.x_0 > 0:
            changed = [[0] * len(self.boxes[0]) for i in range(len(self.boxes))]
            for i in range(len(self.boxes)):
                for k in range(len(self.boxes[0])):
                    changed[i][k] = self.boxes[i][k]

            changed[self.x_0][self.y_0] = changed[self.x_0-1][self.y_0]
            changed[self.x_0-1][self.y_0] = 0
            self.movements.append(Box(changed))

        if self.x_0 < len(self.boxes)-1:
            changed = [[0] * len(self.boxes[0]) for i in range(len(self.boxes))]
            for i in range(len(self.boxes)):
                for k in range(len(self.boxes[0])):
                    changed[i][k] = self.boxes[i][k]

            changed[self.x_0][self.y_0] = changed[self.x_0+1][self.y_0]
            changed[self.x_0+1][self.y_0] = 0
            self.movements.append(Box(changed))

        if self.y_0 > 0:
            changed = [[0] * len(self.boxes[0]) for i in range(len(self.boxes))]
            for i in range(len(self.boxes)):
                for k in range(len(self.boxes[0])):
                    changed[i][k] = self.boxes[i][k]

            changed[self.x_0][self.y_0] = changed[self.x_0][self.y_0-1]
            changed[self.x_0][self.y_0-1] = 0
            self.movements.append(Box(changed))

        if self.y_0 < len(self.boxes[0])-1:
            changed = [[0] * len(self.boxes[0]) for i in range(len(self.boxes))]
            for i in range(len(self.boxes)):
                for k in range(len(self.boxes[0])):
                    changed[i][k] = self.boxes[i][k]

            changed[self.x_0][self.y_0] = changed[self.x_0][self.y_0+1]
            changed[self.x_0][self.y_0+1] = 0
            self.movements.append(Box(changed))

        return self.movements

    def manhattan(self, goal):
        self.distance = 0
        for i in range(len(self.boxes)):
            for k in range(len(self.boxes[0])):
                if goal.boxes[i][k] != 0:
                    self.distance = self.distance + abs(self.coord[goal.boxes[i][k]][0]-i) + abs(self.coord[goal.boxes[i][k]][1]-k)

        return self.distance

    def show(self):
        for i in range(len(self.boxes)):
            for k in range(len(self.boxes[0])):
                print('{:2}'.format(self.boxes[i][k]), " ", end='')
            print("")
        print("")

    def equal(self, goal):
        for i in range(len(self.boxes)):
            for k in range(len(self.boxes[0])):
                if goal.boxes[i][k] != self.boxes[i][k]:
                    return False
        return True


class Game:
    def __init__(self, box, final_box):
        self.box = box
        self.final_box = final_box

        print("Greedy")
        cost_a = self.greedy()
        print(cost_a)
        print("")
        print("A*")
        cost_b = self.a_star()
        print(cost_b)

    def greedy(self):
        pq = []

        start_node = Node(self.box)
        goal_node = Node(self.final_box)

        start_node.f = start_node.value.manhattan(goal_node.value)
        start_node.g = 0
        pq.append([start_node.f, start_node])
        #heapq.heappush(pq, (start_node.f, start_node))

        while len(pq) > 0:
            pq.sort(key = lambda tup: tup[0], reverse=True)
            f, node = pq.pop()
            #f, node = heapq.heappop(pq)

            if node.closed is False:
                node.value.show()
                node.closed = True

                successors = node.value.neighbors()

                for successor in successors:
                    node_successor = Node(successor)

                    cost = 1
                    h = node_successor.value.manhattan(goal_node.value)

                    if node_successor.closed is False:
                        node_successor.g = node.g + cost
                        node_successor.f = h

                        if node_successor.value.equal(goal_node.value):
                            return node_successor.g

                        pq.append([node_successor.f, node_successor])
                        #heapq.heappush(pq, (node_successor.f, node_successor))

    def a_star(self):
        pq = []

        start_node = Node(self.box)
        goal_node = Node(self.final_box)

        start_node.f = start_node.value.manhattan(goal_node.value)
        start_node.g = 0
        pq.append([start_node.f, start_node])
        # heapq.heappush(pq, (start_node.f, start_node))

        while len(pq) > 0:
            pq.sort(key=lambda tup: tup[0], reverse=True)
            f, node = pq.pop()
            # f, node = heapq.heappop(pq)

            if node.closed is False:
                node.value.show()
                node.closed = True

                if node.value.equal(goal_node.value):
                    return node.g

                successors = node.value.neighbors()

                for successor in successors:
                    node_successor = Node(successor)

                    cost = 1
                    h = node_successor.value.manhattan(goal_node.value)

                    if node_successor.closed is False and node_successor.f > node.g + cost + h:
                        node_successor.g = node.g + cost
                        node_successor.f = node_successor.g + h

                        pq.append([node_successor.f, node_successor])
                        # heapq.heappush(pq, (node_successor.f, node_successor))


if __name__ == '__main__':
    nRows = 9
    nColumns = 9

    final = [[0]*nColumns for i in range(nRows)]
    for i in range(nRows):
        for j in range(nColumns):
            if i == nRows-1 and j == nColumns-1:
                final[i][j] = 0
            else:
                final[i][j] = i*nColumns + j + 1
    final_box = Box(final)

    initialBoxes_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [10, 11, 12, 13, 14, 15, 16, 17, 18],
                      [19, 20, 21, 22, 23, 24, 25, 26, 27],
                      [28, 29, 30, 31, 32, 33, 34, 35, 36],
                      [37, 38, 39, 40, 41, 42, 43, 44, 45],
                      [46, 47, 48, 49, 50, 51, 52, 53, 54],
                      [55, 56, 57, 58, 59, 0, 61, 62, 63],
                      [64, 65, 66, 67, 68, 60, 71, 79, 72],
                      [73, 74, 75, 76, 77, 69, 78, 70, 80]]
    box_1 = Box(initialBoxes_1)

    initialBoxes_2 = [[10, 44, 27, 28, 61, 8, 14, 17, 0],
                      [22, 6, 16, 43, 48, 51, 36, 2, 68],
                      [24, 38, 37, 45, 18, 41, 70, 34, 46],
                      [55, 4, 1, 30, 50, 58, 32, 12, 9],
                      [3, 23, 60, 56, 40, 15, 72, 54, 20],
                      [7, 25, 11, 47, 5, 74, 29, 35, 26],
                      [52, 57, 73, 65, 49, 42, 77, 78, 21],
                      [31, 67, 13, 53, 62, 66, 80, 33, 69],
                      [39, 75, 64, 19, 59, 76, 63, 79, 71]]
    box_2 = Box(initialBoxes_2)

    game_1 = Game(box_1, final_box)

