class Game:
    def __init__(self,a,c,m):
        self.grid = [[True for i in range(10)] for j in range(10)]
        self.a,self.c,self.m,self.r = a,c,m,0

    def translate(self,coords):
        return 9-coords[1],coords[0]

    def calculate(self):
        self.r = (self.a * self.r + self.c) % self.m
        x = int(str(self.r)[-1])
        if self.r < 10:
            y = 0
        else:
            y = (self.r % 100)//10
        self.r = (self.a * self.r + self.c) % self.m
        if self.r % 2 == 0:
            orient = "h"
        else:
            orient = "v"
        return (x,y),orient

    def valid(self,coords,orient,length):
        row,col = self.translate(coords)
        if orient == "h":
            for c in range(col,col+length):
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= row + i <= 9 and 0 <= c + j <= 9:
                            if not self.grid[row+i][c+j]: return False
                        elif i == 0 and j == 0: return False
        else:
            for r in range(row,row-length,-1):
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= r + i <= 9 and 0 <= col + j <= 9:
                            if not self.grid[r+i][col+j]: return False
                        elif i == 0 and j == 0: return False
        return True

    def place(self,coords,orient,length):
        row, col = self.translate(coords)
        if orient == "h":
            for c in range(col,col+length):
                self.grid[row][c] = False
        else:
            for r in range(row,row-length,-1):
                self.grid[r][col] = False

    def move(self,length):
        placed = False
        while not placed:
            coords,orient = self.calculate()
            placed = self.valid(coords,orient,length)
        self.place(coords,orient,length)
        return coords,orient

    def play(self):
        order = [4,3,3,2,2,2,1,1,1,1]
        for length in order:
            coords,orient = self.move(length)
            print (coords[0],coords[1],orient)

    def output(self):
        for i in range(10):
            print (*self.grid[i])

a,b,c = map(int , input().split())
g = Game(a,b,c)
g.play()