U, R, D, L = 0, 1, 2, 3

def rotate(cur, dir):
    if dir == 'F': return cur
    if dir == 'L': return (cur - 1 + 4) % 4
    if dir == 'R': return (cur + 1) % 4

class Game:
    def __init__(self, n):
        self.n = n
        self.dir = U
        self.pos = (0,0)
        self.positions = []

    def move(self, com):
        self.positions.append(self.pos)
        if len(self.positions) > self.n:
            self.positions = self.positions[1:]
        cant_move = False
        for i in range(4):
            self.dir = rotate(self.dir, com)
            x, y = self.pos
            if self.dir == L: newpos = (x - 1, y)
            elif self.dir == R: newpos = (x + 1, y)
            elif self.dir == U: newpos = (x, y + 1)
            elif self.dir == D: newpos = (x, y - 1)

            if newpos in self.positions:
                cant_move = True
                com = "R"
            else:
                self.pos = newpos
                cant_move = False
                break
        return not cant_move

n, instructions, moves = input().split(" ")
n,moves = int(n),int(moves)
game = Game(n)
for i in range(moves):
    com = instructions[i % len(instructions)]
    canmove = game.move(com)
    if not canmove: break
print(game.pos)