class WinDoor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        self.square = self.x * self.y
        return self.square

class Room(WinDoor):
    def __init__(self, x, y, z):
        WinDoor.__init__(self, x, y)
        self.z = z
        self.wd = []
        self.total_square = 0

    def square(self):
        self.square = 2 * self.z * (self.x + self.y)
        return self.square

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))

    def workSurface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= WinDoor.square(i)
        self.total_square = new_square
        return new_square

    def roll_numb(self, w, h):
        return self.total_square / (w * h)
        

r1 = Room(float(input('Введите ширину: ')), float(input('Введите длинну: ')), float(input('Введите высоту: ')))
r1.addWD(1, 1) 
r1.addWD(1, 1)
r1.addWD(1, 2)
print(f'Общая площадь: {r1.workSurface()}')
print(f'Количество рулонов: {r1.roll_numb(3, 4)}')