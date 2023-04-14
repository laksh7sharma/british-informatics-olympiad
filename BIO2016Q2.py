class Game:
    def __init__(self, start, seq, moves):
        self.grid = [[0 for i in range(101)] for j in range(101)]
        self.start, self.seq, self.moves = start, seq, moves

    def move(self, coords):
        r, c = coords
        if self.grid[r][c] >= 4:
            self.grid[r][c] -= 4
            overcrowded = []
            adj = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for neighbour in adj:
                x, y = neighbour
                self.grid[x][y] += 1
                if self.grid[x][y] >= 4:
                    overcrowded.append((x, y))

            for neighbour in overcrowded:
                self.move(neighbour)

    def translate(self, num):
        x, y = (num - 1) // 5, (num - 1) % 5
        return x + 48, y + 48

    def play(self):
        next = self.start
        while True:
            for num in self.seq:
                if self.moves == 0: return
                if next > 25: next -= 25
                coords = self.translate(next)
                self.grid[coords[0]][coords[1]] += 1
                self.move(coords)
                self.moves -= 1
                next += num

    def output(self):
        for i in range(48, 53):
            print (*self.grid[i][48:53])


start, length, moves = map(int, input().split())
sequence = list(map(int, input().split()))
g = Game(start, sequence, moves)
g.play()
g.output()