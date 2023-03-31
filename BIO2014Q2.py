from collections import defaultdict

class Game:
    def __init__(self, n, grid):
        self.n = n
        self.g = defaultdict(list)
        self.r = defaultdict(list)
        self.grid = grid
        self.gpoints = 0
        self.rpoints = 0
        self.visited = set()
        self.found = {"g" : set() , "r" : set()}
        for r in range(self.n - 1, -1, -1):
            for c in range(self.n):
                n1 = (2 * r, 2 * c + 1)  # up
                n2 = (2 * r + 1, 2 * c + 2)  # right
                n3 = (2 * r + 2, 2 * c + 1)  # down
                n4 = (2 * r + 1, 2 * c)  # left
                type = self.grid[r][c]
                if type == 1:
                    self.r[n1].append(n3)
                    self.r[n3].append(n1)
                    self.g[n2].append(n4)
                    self.g[n4].append(n2)
                elif type == 2:
                    self.r[n2].append(n4)
                    self.r[n4].append(n2)
                    self.g[n1].append(n3)
                    self.g[n3].append(n1)
                elif type == 3:
                    self.r[n4].append(n1)
                    self.r[n1].append(n4)
                    self.g[n2].append(n3)
                    self.g[n3].append(n2)
                elif type == 4:
                    self.r[n1].append(n2)
                    self.r[n2].append(n1)
                    self.g[n3].append(n4)
                    self.g[n4].append(n3)
                elif type == 5:
                    self.r[n2].append(n3)
                    self.r[n3].append(n2)
                    self.g[n4].append(n1)
                    self.g[n1].append(n4)
                elif type == 6:
                    self.r[n3].append(n4)
                    self.r[n4].append(n3)
                    self.g[n1].append(n2)
                    self.g[n2].append(n1)

    def cycle(self):
        for node in self.g:
            if node not in self.found["g"]:
                self.visited = set()
                dist = self.dfs(node,"g",node,0, None)
                if dist != 0:
                    self.gpoints += dist
        for node in self.r:
            if node not in self.found["r"]:
                self.visited = set()
                dist = self.dfs(node,"r",node,0, None)
                if dist != 0:
                    self.rpoints += dist
        print (self.rpoints , self.gpoints)

    def dfs(self, node, col, source, d, previous):
        self.visited.add(node)
        if node == source and d > 0:
            self.found[col] = self.found[col].union(self.visited)
            return d
        if col == "g":
            for child in self.g[node]:
                if child != node and child != previous:
                    return self.dfs(child,col,source, d + 1, node)
        else:
            for child in self.r[node]:
                if child != node and child != previous:
                    return self.dfs(child,col,source, d + 1, node)
        return 0

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int , input().split())))
g = Game(n, arr)
g.cycle()

