from datetime import date

class Person:
    def __init__(self, name, age):
        print('Init of Person called')
        self.name = name
        self.age = age

    @classmethod
    def fromBirth(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age>18

    def show_info(self):
        print('Name is {} and age is {}'.format(self.name, self.age))


class Indian(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.country = 'India'
        print('Init of Indian called')

    # def show_info(self):
    #     print('Name is {} and age is {}. Person is from {}'.format(self.name, self.age, self.country))


i1 = Indian('kunal', 20)
i1.show_info()

i2 = Indian.fromBirth('kk', 2000)
i2.show_info()
