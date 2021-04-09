class WinDoor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        self.square = self.x * self.y
        return self.square

class Room:
    def __init__(self, x, y, z):
        WinDoor.__init__(self, x, y)
        self.z = z
        self.wd = []

    def square(self):
        self.square = 2 * self.z * (self.x + self.y)
        return self.square

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))

    def workSurface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= WinDoor.square(i)
        return new_square
 

r1 = Room(float(input('Введите ширину: ')), float(input('Введите длинну: ')), float(input('Введите высоту: ')))
r1.addWD(1, 1) 
r1.addWD(1, 1)
r1.addWD(1, 2)
print(f'Общая площадьв: {r1.workSurface()}')