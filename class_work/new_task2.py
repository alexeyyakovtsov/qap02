class IncapsTest:
    def __init__(self, field):
        self.__privite_field = field

    def show_privite_field(self):
        return self.__privite_field

a = IncapsTest('test')
print(a.show_privite_field())
