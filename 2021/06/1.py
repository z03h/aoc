with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

line = lines[0]


class Fish:
    def __init__(self, spawn_time, *, index=None):
        self.spawn_time = spawn_time
        self.index = index if index is not None else spawn_time

    def spawn(self):
        cls = type(self)
        return cls(7, index=8)

    def decrement(self):
        self.index -= 1
        if self.index < 0:
            self.index = self.index % self.spawn_time
            return self.spawn()
        return False


fishies = [Fish(7, index=int(i)) for i in line.split(',')]

days = 80
for _ in range(days):
    to_add = []
    for fish in fishies:
        f = fish.decrement()
        if f:
            to_add.append(f)

    if to_add:
        fishies.extend(to_add)

print(len(fishies))
