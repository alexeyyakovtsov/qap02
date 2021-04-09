class WinDoor:
    def __init__(self, x, y, name="unk"):
       self.x = x
       self.y = y
       self.name = name

    def square(self):
       self.square = self.x * self.y 

    #getter
    def __repr__(self):
       return f'{self.name} {self.x}x{self.y}'

class Room(WinDoor):
    def __init__(self,x, y, z):
        WinDoor.__init__(self, x, y, z)
        self.z = z
        self.wd = []

    def square(self):
        self.square = 2 * self.z * (self.x + self.y)
        print(f'Полная площадь = {self.square}')

    #setter
    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))
        
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        print(f'Оклеиваемая площадь = {new_square}')
        return new_square

r1 = Room(int(input('Введите ширину: ')), int(input('Введите длинну: ')), int(input('Введите высоту: ')))
r1.square()
r1.addWD(1, 1) 
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.wd)
r1.workSurface()