class Game:
    def __init__(self, p, arr):
        self.countPlayers = p
        self.perimeter = [(0,0)]
        self.grid = {(0,0) : 0}
        self.start = (0,0)
        self.players = {i : (0,0,"L") for i in range(1,p+1)}
        self.moves = {i + 1: el for i,el in enumerate(arr)}
        self.opposite = {"U" : "D" , "D" : "U" , "L" : "R" , "R" : "L"}
        self.player = 1
        self.lengthPerimeter = 3

    def is_up(self,coordinates):
        x,y = coordinates
        return x % 2 == y % 2

    def next_edge(self,coordinates,edge):
        if self.is_up(coordinates):
            order = {"L": "R", "R": "D", "D": "L"}
        else:
            order = {"L": "U", "U": "R", "R": "L"}

        return order[edge]

    def adjTriangle(self,coordinates,direction):
        x, y = coordinates
        if self.is_up(coordinates):
            adjascent = {"L": (x - 1, y), "R": (x + 1, y), "D": (x, y - 1)}
        else:
            adjascent = {"L": (x - 1, y), "R": (x + 1, y), "U": (x, y + 1)}

        return adjascent[direction]

    def nextTriangle(self,coordinates,direction):
        x,y = coordinates
        # if self.is_up(coordinates):
        #     adjascent = {"L": (x - 1, y), "R": (x + 1, y), "D": (x, y - 1)}
        # else:
        #     adjascent = {"L": (x - 1, y), "R": (x + 1, y), "U": (x, y + 1)}
        # if adjascent[direction] in self.perimeter:
        #     return adjascent[direction],self.opposite[direction]  # not opposite

        if self.is_up(coordinates):
            order = [(x,y+1,"L") , (x+1,y+1,"L") , (x+1,y,"U")]
        else:
            order = [()]


        return coordinates,self.next_edge(coordinates,direction)

    def leftMost(self):
        left = (0,0)
        for coords in self.perimeter:
            x,y = coords
            if x < left[0]: left = (x,y)
            elif x == left[0] and y > left[1]: left = (x,y)
        return left

    def traverse(self):
        coords, dir = (self.players[self.player][0], self.players[self.player][1]), self.players[self.player][2]
        toFill,toFilldir = coords, dir
        for i in range(self.moves[self.player]):
            coords,dir = self.nextTriangle(coords,dir)
        self.fill(toFill,toFilldir)
        self.reposition()
        self.player = self.player + 1
        if self.player > self.countPlayers: self.player = 1
        
    def fill(self,coordinates, direction):
        x,y = self.adjTriangle(coordinates,direction)
        print(x, y)
        self.grid[(x,y)] = self.player
        self.perimeter.append((x,y))

    def reposition(self):
        reposition = []
        for player,pos in self.players.items():
            coords,dir = (self.players[player][0], self.players[player][1]), self.players[player][2]
            x,y = self.adjTriangle(coords,dir)
            if (x,y) in self.perimeter: reposition.append(player)
        coords = self.leftMost()
        for player in reposition:
            self.players[player] = (coords[0], coords[1], "L")

    def findLength(self):
        s = self.leftMost()
        print (s)
        c,d,i = s,"L",0
        for j in range(10):
            c,d = self.nextTriangle(c,d)
            print ((c,d) , end = " ")
            i += 1
            if c == s and d == "L":
                self.lengthPerimeter = i
                break
        print (self.lengthPerimeter)

players,moves = 2,5
arr = [16,2]
g = Game(players,arr)
for i in range(moves):
    g.traverse()
    print (g.perimeter)
    print (g.grid)
    g.findLength()
print (g.lengthPerimeter)