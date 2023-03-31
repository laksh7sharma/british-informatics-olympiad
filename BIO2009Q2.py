from collections import deque

class Game:
    def __init__(self,grid):
        self.grid = grid
        self.original = [row[:] for row in self.grid]
        self.counters = [3 for i in range(4)]
        self.visited = [[False for i in range(4)] for j in range(4)]
        self.removed = [[False for i in range(4)] for j in range(4)]
        self.points = 0
        self.temp = 1
        self.flag = False

    def adjust(self):

        for r in range(4):
            for c in range(4):
                if self.removed[r][c]:
                    self.grid[r][c] = ""

        for i in range(3):
            for c in range(4):
                for r in range(3,-1,-1):
                    if self.grid[r][c] == "" and r != 0:
                        self.grid[r][c] = self.grid[r-1][c]
                        self.grid[r-1][c] = ""

        free = [0 for i in range(4)]

        for c in range(4):
            for r in range(3, -1, -1):
                if self.grid[r][c] == "":
                    self.grid[r][c] = self.original[self.counters[c]][c]
                    self.counters[c] = (self.counters[c] + 3) % 4

    def bfsGrid(self, r, c):
        colour = self.grid[r][c]
        qu = deque()
        qu.append([r, c])
        connected = set()

        while len(qu) > 0:
            el = qu.popleft()
            r, c = el[0], el[1]
            connected.add((r,c))
            self.visited[r][c] = True
            dy = [0 + r, 0 + r, -1 + r, 1 + r]
            dx = [-1 + c, 1 + c, 0 + c, 0 + c]
            for i in range(4):
                nr = dy[i]
                nc = dx[i]
                if not (0 <= nr < 4 and 0 <= nc < 4): continue
                if not self.visited[nr][nc] and self.grid[nr][nc] == colour:
                    qu.append([nr, nc])

        if len(connected) >= 2:
            self.temp *= len(connected)
            for item in connected:
                self.removed[item[0]][item[1]] = True
                self.flag = True

    def remove(self):
        self.visited = [[False for i in range(4)] for j in range(4)]
        self.removed = [[False for i in range(4)] for j in range(4)]
        self.temp = 1
        self.flag = False
        for r in range(4):
            for c in range(4):
                self.bfsGrid(r,c)
        if not self.flag:
            print ("Game Over")
            return False
        else:
            self.points += self.temp
            self.adjust()
            return True

    def output(self):
        for row in self.grid:
            print ("".join(row))
        print (self.points)

arr = []
for i in range(4):
    arr.append(list(str(input())))
g = Game(arr)
inp = int(input())
res = True
while inp != 0 and res:
    for i in range(inp):
        res = g.remove()
        if not res:
            break
    g.output()
    if res:
        inp = int(input())