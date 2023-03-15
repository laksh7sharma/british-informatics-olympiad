class Lights:
    def __init__(self, characters):
        self.grid = [[0 for i in range(5)] for j in range(5)]
        self.characters = characters
        for char in self.characters:
            if char.isupper():
                num = ord(char) - 65
                k = 2
            else:
                num = ord(char) - 97
                k = 1
            r, c = divmod(num, 5)
            self.grid[r][c] = k

    def combinations(self):
        perm = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        for m in range(3):
                            perm.append([i, j, k, l, m])
        return perm

    def play(self):
        perm = self.combinations()
        for CurrentRow in perm:
            pref = ""
            copy = [row[:] for row in self.grid]
            for i in range(5):
                copy = self.update(copy, 0, i, CurrentRow[i])
                val = CurrentRow[i]
                if val == 1: pref = pref + chr(97 + i)
                elif val == 2: pref = pref + chr(65 + i)

            res, pattern = self.check(1, copy, pref)
            if res:
                print(pattern)
                return
        print ("impossible")

    def update(self,grid,r,c,count):
        dy = [0 + r, 0 + r, -1 + r, 1 + r, r]
        dx = [-1 + c, 1 + c, 0 + c, 0 + c, c]
        for i in range(5):
            nr,nc = dy[i], dx[i]
            if 0 <= nr <= 4 and 0 <= nc <= 4:
                grid[nr][nc] = (grid[nr][nc] + count) % 3
        return grid

    def check(self, row, g, previous):
        grid = [row[:] for row in g]
        copy = previous
        if row == 5:
            total = 0
            for r in grid:
                total += sum(r)
            return total == 0, copy
        for c in range(5):
            if grid[row - 1][c] == 1:
                copy += chr(65 + 5 * row + c)
                grid = self.update(grid, row, c, 2)
            elif grid[row - 1][c] == 2:
                copy += chr(97 + 5 * row + c)
                grid = self.update(grid, row, c, 1)
        return self.check(row + 1, grid, copy)

g = Lights(input())
g.play()