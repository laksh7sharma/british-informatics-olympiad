class Game:
    def __init__(self, initialRegion):
        self.Grid = [[1 for i in range(11)] for j in range(11)]
        for i,row in enumerate(initialRegion):
            for j,el in enumerate(row):
                self.Grid[4 + i][4 + j] = el
        self.directionVector = {0 : (-1,0), 1: (0,1), 2: (1,0), 3:(0,-1)}
        self.heading = 0
        self.DieOrient = {"Upper" : 1, "Touch" : 6, "Top" : 2, "Bottom" : 5, "Left" : 3, "Right" : 4}
        self.DieCoordinates = (5, 5)

    def rotate(self):
        if self.heading == 0:
            self.DieOrient["Top"], self.DieOrient["Touch"], self.DieOrient["Bottom"], self.DieOrient["Upper"] = self.DieOrient["Upper"], self.DieOrient["Top"], self.DieOrient["Touch"], self.DieOrient["Bottom"]
        elif self.heading == 1:
            self.DieOrient["Right"], self.DieOrient["Touch"], self.DieOrient["Left"], self.DieOrient["Upper"] = self.DieOrient["Upper"], self.DieOrient["Right"], self.DieOrient["Touch"], self.DieOrient["Left"]
        elif self.heading == 2:
            self.DieOrient["Top"], self.DieOrient["Touch"], self.DieOrient["Bottom"], self.DieOrient["Upper"] = self.DieOrient["Touch"], self.DieOrient["Bottom"], self.DieOrient["Upper"], self.DieOrient["Top"]
        else:
            self.DieOrient["Right"], self.DieOrient["Touch"], self.DieOrient["Left"], self.DieOrient["Upper"] = self.DieOrient["Touch"], self.DieOrient["Left"], self.DieOrient["Upper"], self.DieOrient["Right"]

    def makeMove(self):
        num = self.DieOrient["Upper"] + self.Grid[self.DieCoordinates[0]][self.DieCoordinates[1]]
        if num > 6: num -= 6
        self.Grid[self.DieCoordinates[0]][self.DieCoordinates[1]] = num
        if num == 1 or num == 6: self.heading = self.heading
        elif num == 2: self.heading = (self.heading + 1) % 4
        elif num == 3 or num == 4: self.heading = (self.heading + 2) % 4
        else: self.heading = (self.heading + 3) % 4
        self.DieCoordinates = self.DieCoordinates[0] + self.directionVector[self.heading][0], self.DieCoordinates[1] + self.directionVector[self.heading][1]
        self.DieCoordinates = self.DieCoordinates[0] % 11, self.DieCoordinates[1] % 11
        self.rotate()

    def output(self):
        n1, n2 = self.DieCoordinates
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= n1 + i < 11 and 0 <= n2 + j < 11:
                    print (self.Grid[n1 + i][n2 + j], end = "")
                else:
                    print ("X", end = "")
            print ("\n".strip())

inputArr = [list(map(int , input().split())) for i in range(3)]
g = Game(inputArr)
while True:
    moves = int(input())
    if moves == 0: break
    for move in range(moves):
        g.makeMove()
    g.output()