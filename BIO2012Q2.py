class Point:
    def __init__(self, char):
        self.isLazy = True
        self.char = char
        self.neigbhours = {"S" : [], "C" : []}
        self.pointSet = ""

    def getNext(self, pointEntered):
        if pointEntered in self.neigbhours["S"]:
            old = self.pointSet
            ind = self.neigbhours["C"].index(old)
            if self.isLazy:
                if pointEntered != old:
                    self.pointSet = self.neigbhours["C"][1 - ind]
            else:
                self.pointSet = self.neigbhours["C"][1 - ind]
            return old
        else:
            return self.neigbhours["S"][0]

class Grid:
    def __init__(self,notLazy,cur,moves):
        self.grid = [Point(chr(65 + i)) for i in range(24)]
        for char in notLazy:
            self.grid[ord(char) - 65].isLazy = False
        self.initialise()
        self.currentPoints = cur
        self.moves = moves

    def initialise(self):
        r1 = [chr(65 + i) for i in range(4)]
        r2 = [chr(69 + i) for i in range(8)]
        r3 = [chr(77 + i) for i in range(8)]
        r4 = [chr(85 + i) for i in range(4)]

        for i in range(4):
            self.grid[i].neigbhours["C"].extend([chr(69 + 2 * i), chr(70 + 2 * i)])
            self.grid[i].neigbhours["S"].append(chr(68 - i))

        for i,el in enumerate(r4):
            self.grid[20 + i].neigbhours["C"].extend([r3[i*2], r3[i*2+1]])
            self.grid[ord(r3[i*2]) - 65].neigbhours["S"].append(el)
            self.grid[ord(r3[i*2 + 1]) - 65].neigbhours["S"].append(el)
            self.grid[20 + i].neigbhours["S"].append(r4[i + 1 if i % 2 == 0 else i - 1])

        for i,el in enumerate(r2):
            self.grid[4 + i].neigbhours["S"].append(r1[i//2])
            self.grid[4 + i].neigbhours["C"].extend([r3[i], r3[(i + 1) % 8]])
            self.grid[ord(r3[i]) - 65].neigbhours["C"].append(el)
            self.grid[ord(r3[(i + 1) % 8]) - 65].neigbhours["C"].append(el)

        for i,char in enumerate(self.grid):
            self.grid[i].pointSet = self.grid[i].neigbhours["C"][0]

    def play(self):
        for i in range(self.moves):
            p1,p2 = self.currentPoints[0], self.currentPoints[1]
            ind1,ind2 = ord(p1) - 65, ord(p2) - 65
            p = self.grid[ind2].getNext(p1)
            self.currentPoints = p2 + p
        print (self.currentPoints)

arr = [input().strip() for i in range(3)]
g = Grid(arr[0], arr[1], int(arr[2]))
g.play()