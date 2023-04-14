import time

class Game:
    def __init__(self,plan):
        self.letters = len(plan) + 2
        self.visits = {chr(65+i) : 0 for i in range(self.letters)}
        self.visits["A"] = 1
        self.exits = {chr(65+i) : [] for i in range(self.letters)}
        self.rooms = {chr(65+i) : [] for i in range(self.letters)}
        self.plan = plan
        self.location = "A"

    def next(self,room):
        if self.visits[room] % 2 == 1:
            self.exits[room][0][1] += 1
            return self.rooms[room][0]
        else:
            for i,exit in enumerate(self.exits[room]):
                nextroom,times = exit[0],exit[1]
                if times % 2 == 1:
                    break

            if self.exits[room][-1] == exit:
                self.exits[room][-1][1] += 1
                return nextroom
            else:
                self.exits[room][i+1][1] += 1
                return self.rooms[room][i+1]

    def create(self):
        chosen = {chr(65+i) : False for i in range(self.letters)}
        notchosen = []

        while len(self.plan) > 0:
            first = self.plan[0]
            self.plan = self.plan[1:]
            for letter,result in chosen.items():
                if not result and letter not in self.plan and letter != first:
                    room = letter
                    break
            chosen[room] = True

            self.rooms[first].append(room)
            self.rooms[room].append(first)

        for letter,result in chosen.items():
            if not result:
                notchosen.append(letter)

        self.rooms[notchosen[0]].append(notchosen[1])
        self.rooms[notchosen[1]].append(notchosen[0])

    def move(self):
        next = self.next(self.location)
        self.visits[next] += 1
        self.location = next

    def output(self):
        for key in self.rooms:
            self.rooms[key].sort()

        for key,room in self.rooms.items():
            for r in room:
                self.exits[key].append([r,0])
            print ("".join(room))

plan,p,q = input().split()
p,q = int(p),int(q)

start = time.time()

g = Game(plan)
g.create()
g.output()
for i in range(q):
    g.move()
    if i == p - 1 or i == q - 1:
        print (g.location , end = "")

end = time.time()
print (end-start)