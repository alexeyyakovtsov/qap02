class Car:
    def __init__(self, color='black', wheels=4, body='crossover'):
        self.color = color
        self.wheels = wheels
        self.body = body
    
    def mvoe(self):
        print('move car')
        self.color = 'rusty'


car = Car()
print(car.wheels)

car2 = Car('white', 4,  'sidan')
print(car2.color)
car2.mvoe()
print(car2.color)
