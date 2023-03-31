class Game:
    def __init__(self,p1,p2):
        self.Grid = [[0 for j in range(5)] for i in range(5)]
        for i in range(5):
            self.Grid[0][i] = i + 11
            self.Grid[4][i] = i + 1
        self.Locations = {i+1 : (4,i) for i in range(5)}
        for i in range(5):
            self.Locations[i+11] = (0,i)
        self.Grid[2][2] = 25
        self.Locations[25] = (2,2)
        self.Orders = {1 : p1 , 2 : p2}
        self.Directions = {1 : (-1,0) , 2 : (-1,1) , 3 : (0,1) , 4 : (1,1) , 5 : (1,0) , 6 : (1,-1) , 7 : (0,-1) , 8 : (-1,-1)}

    def move(self,r,c,direction):
        row,col = r,c
        piece = self.Grid[row][col]
        self.Grid[row][col] = 0
        while True:
            if self.Grid[row][col] == 0 and 0 <= row <= 4 and 0 <= col <= 4 and 0 <= row + self.Directions[direction][0] <= 4 and 0 <= col + self.Directions[direction][1]<= 4:
                if self.Grid[row + self.Directions[direction][0]][col + self.Directions[direction][1]] == 0:
                    row,col = row + self.Directions[direction][0] , col + self.Directions[direction][1]
                else:
                    break
            else:
                break
        self.Grid[row][col] = piece
        self.Locations[piece] = (row,col)

    def willWin(self,player,chosen):
        r,c = self.Locations[25]
        if player == 2: otherPlayer = 1
        else: otherPlayer = 2
        a = {1 : [] , 2 : []}
        other = []

        for direction in range(1,9):
            row, col = r, c
            while True:
                if 0 <= row <= 4 and 0 <= col <= 4:
                    if 0 <= row + self.Directions[direction][0] <= 4 and 0 <= col + self.Directions[direction][1] <= 4:
                        if self.Grid[row + self.Directions[direction][0]][col + self.Directions[direction][1]] == 0:
                            row, col = row + self.Directions[direction][0], col + self.Directions[direction][1]
                        else:
                            break
                    else:
                        break
                else:
                    break
            if row == 0: a[2].append(direction)
            elif row == 4: a[1].append(direction)
            else: other.append(direction)

        if len(a[player]) > 0:
            return a[player][0],True
        elif len(a[otherPlayer]) == 8:
            return a[otherPlayer][0],True
        else:
            for direction in other:
                row,col = r,c
                while True:
                    if 0 <= row <= 4 and 0 <= col <= 4:
                        if 0 <= row + self.Directions[direction][0] <= 4 and 0 <= col + self.Directions[direction][1] <= 4:
                            if self.Grid[row + self.Directions[direction][0]][col + self.Directions[direction][1]] == 0:
                                row, col = row + self.Directions[direction][0], col + self.Directions[direction][1]
                            else:
                                break
                        else:
                            break
                    else:
                        break
                valid = True
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if chosen[0]+i == row and chosen[1]+j == col:
                            valid = False
                if valid and not (row == r and col == c):
                    #print (row,col)
                    return direction,False
            return 1,False

    def play(self):
        done = False
        while not done:
            for i in range(5):
                for player in range(1,3):
                    if player == 2: chosen = self.Locations[self.Orders[player][i]+10]
                    else: chosen = self.Locations[self.Orders[player][i]]
                    dir,done = self.willWin(player,chosen)
                    r,c = self.Locations[25]
                    self.move(r,c,dir)
                    if done: return
                    r,c = chosen
                    for direction,coord in self.Directions.items():
                        if not (0 <= r + coord[0] <= 4 and 0 <= c + coord[1] <= 4): continue
                        if self.Grid[r + coord[0]][c + coord[1]] == 0:
                            self.move(chosen[0],chosen[1],direction)
                    if i == 0: self.output()

    def output(self):
        for i in range(5):
            for j in range(5):
                if self.Grid[i][j] == 0: print ("." , end = " ")
                elif 10 > self.Grid[i][j] > 0: print ("F" , end = " ")
                elif self.Grid[i][j] == 25: print ("*" , end = " ")
                else: print ("S" , end = " ")
            print ("\n")
        print ("\n")

p1 = list(map(int , input().split()))
p2 = list(map(int , input().split()))
g = Game(p1,p2)
g.play()
g.output()