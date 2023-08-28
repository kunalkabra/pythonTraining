def make_pretty(func):
    def inner():
        print("I got decorated")
        return func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()

#
# print(__name__)

#
# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a
#     # Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # a static method to check if a
#     # Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
#
# print(person1.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(22))


def product(a, b):
    p = a * b
    print(p)

product(1,2)

# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)

# # Uncommenting the below line shows an error
# # product(4, 5)
#
# # This line will call the second product method
# product(4, 5)













# def smart_divide(func):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#     return inner
#
#
# def divide_num(a, b):
#     print(a/b)
#
# divide_num = smart_divide(divide_num)
#
# divide_num(2, 4)
# divide_num(4, 2)


# print(__name__)



# class Computer:
#     year = 2001
#
#     def __init__(myself, cpu, ram):
#         myself.cpu = cpu
#         myself.ram = ram
#         myself.company = 'HP'
#
#     def show_config(myself):
#         print(f'Config is - cpu: {myself.cpu} '
#               f'and ram: {myself.ram} and company: {myself.company}')
#
#     @staticmethod
#     def show_year():
#         print('Current year')
#
#
# comp1 = Computer('i5', 8)
# comp2 = Computer('i7', 16)
#
#
# # comp2.show_year()
#
# comp1.show_config()
# comp2.show_config()
#


# print(f'Comp1 cpu {comp1.cpu} and ram {comp1.ram}gb')
# print(f'Comp2 cpu {comp2.cpu} and ram {comp2.ram}gb')


# Computer.config(comp1)




class A:
    def __init__(self):
        print("Init of A")

    def test_print(self):
        print("I am in class A")

class Child1(A):
    def __init__(self):
        print("Init of child1")

    def test_print(self):
        print("I am in child1 method")

class Child2(A):
    def __init__(self):
        print("Init of child2")

    def test_print(self):
        print("I am in child2 method")


# sample = Child1()
# sample2 = Child2()

# sample.test_print()
# sample2.test_print()

class C(Child2, Child1):
    def __init__(self):
        print("I am in C")

test = C()



# class MyError(Exception):
#     message="This is my custom error"
#
# # a,b = 2,0
#
# def do_something(n):
#     if n>10:
#         raise MyError("I raised it")
#
# try:
#     do_something(154)
#
# except MyError as e:
#     print("Caught an error", e, e.message)
# except Exception as e:
#     print("Caught an error", e)
#
#





#
#
# else:
#     print("No error found")
# finally:
#     print("connection Closed")
#
#
# print("I tried")


#
# import timeit
# print(timeit.timeit('''
# def test():
#     print("this is good")
#     '''))


# import time
# start = time.perf_counter()
#
# print("this is good")
# time.sleep(1)
#
# end = time.perf_counter()
#
# print(f'time taken {end-start:0.4f}')