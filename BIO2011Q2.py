from collections import deque

class Game:
    def __init__(self, order):
        self.order = order
        self.cards = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
        self.table = []
        self.stack = [1 for i in range(52)]

    def merge(self,ind1,ind2):
        top = self.table.pop(ind2)
        size = self.stack.pop(ind2)
        self.table[ind1] = top
        self.stack[ind1] += size

    def shuffle(self):
        cards = deque(self.cards[:])
        while True:
            for el in self.order:
                for i in range(el - 1):
                    if len(cards) == 0: return
                    cards.rotate(-1)
                if len(cards) == 0: return
                self.table.append(cards.popleft())

    def valid(self,ind):
        arr = []
        c1 = self.table[ind]
        if 0 <= ind - 1:
            arr.append(self.table[ind - 1])
        if 0 <= ind - 3:
            arr.append(self.table[ind - 3])
        valid = [el for el in arr if (el[0] == c1[0] or el[1] == c1[1])]  # in order of adjascent then separated
        return valid

    def allValid(self,ind1,ind2):
        tot = 0
        table = self.table[:]
        stack = self.stack[:]
        top = self.table.pop(ind2)
        size = self.stack.pop(ind2)
        self.table[ind1] = top
        self.stack[ind1] += size
        for ind in range(len(self.table)):
            tot += len(self.valid(ind))  # need to return table and stack
        self.table = table[:]
        self.stack = stack[:]
        return tot

    def strat1(self):
        for ind in range(len(self.table) - 1,-1,-1):
            arr = self.valid(ind)
            if len(arr) > 0:
                if arr[0] == self.table[ind - 1]: neigbhour = ind - 1
                else: neigbhour = ind - 3
                return ind, neigbhour
        return 0,0

    def strat2(self):
        bestOption = [0,0,0]
        for ind in range(len(self.table) - 1,-1,-1):
            arr = self.valid(ind)
            size = self.stack[ind]
            for el in arr:
                if el == self.table[ind - 1]:
                    neigbhour = ind - 1
                else:
                    neigbhour = ind - 3
                size += self.stack[neigbhour]
                if size > bestOption[0]:
                    bestOption = [size, ind, neigbhour]
                size = self.stack[ind]  # resetting the value of size
        return bestOption[1], bestOption[2]

    def strat3(self):
        bestOption = [0,0,0]
        for ind in range(len(self.table) - 1,-1,-1):
            neigbhours = self.valid(ind)
            for neigbhour in neigbhours:
                if neigbhour == self.table[ind - 1]: adj = ind - 1
                else: adj = ind - 3
                length = self.allValid(adj,ind)
                if length > bestOption[0]:
                    bestOption = [length, ind, adj]
                elif length == 0 and bestOption[0] == 0:
                    bestOption = [length, ind, adj]

        return bestOption[1], bestOption[2]

    def play(self, number):
        functions = {1 : self.strat1, 2 : self.strat2, 3 : self.strat3}
        f = functions[number]
        while len(self.table) >= 1:
            ind, neigbhour = f()
            if ind == 0 and neigbhour == 0:
                break
            self.merge(neigbhour,ind)

order = list(map(int , input().split()))
for i in range(1,4):
    g = Game(order)
    g.shuffle()
    if i == 1: print (g.table[0], g.table[-1])
    g.play(i)
    print (len(g.stack), g.table[0])