# x = list(range(10))

# for val in x:
#     if val % 2 == 0:
#         print('Divisible by 2 : {}'.format(val))
#     elif val % 3 == 0:
#         print(f'Divisible by 3 but not by 2: {val}')


# i = 1
# while i <= 5:
#     print('#', end='')
#     i = i+1


# # # #
# # #
# #
#

#
for i in range(5):
    for j in range(5-i):
        print('#', end='')
        if j%2==0:
            print('i', end='')
            # break
        # print('k', end='')
    # else:
    #     print('There was a break!')
    print()



'How are you doing?'

#
# 'Kunal'
#
#
# for index, val in enumerate('kunal'):
#     print(f'{index}: {val}')


# num_list = [3,5,7,9]
#
# for num in num_list:
#     if (num%2)==0:
#         print("list contains an even number")
#         break
# else:
#     print('list does not contain an even number')

# num = 7
# for i in range(2, num):
#     if (num%i)==0:
#         print('It\'s not a prime number')
#         break
# else:
#     print('It\'s a prime number')


# x = '!!!hi, how are !!!! you!'
#
# print(x)
# print(x.strip('!'))



# var = 'Kunal'
# var = list(var)
# print(f'Start with: {var}')
# for x in var:
#     print(x)
#     var += x
# print(f'End with: {var}')


# var = ['a', 'b', 'c', 'd']
#
# for index, x in enumerate(var):
#     print(index, end=' ')
#     print(x)
#     var.pop(index)
#
# print(var)



'''
list comprehension -> expression for item in iterable (if condition)
'''

# output=[]
#
# def get_num(x):
#     if x%2==0:
#         return output.insert(0,x)
#
# for x in range(9):
#     get_num(x)
#
# # output = [x for x in range(9) if x % 2 == 0 ]
# print(output)



# output = {y for y in range(100) if y%2==0 if y%5==0}
# print(output)



# output = ['Even' if x%2==0 else 'Odd' for x in range(9)]
# print(output)



# var = 'Hi, how are you?'
#
# print(var.startswith('Hi'))
# print(var.endswith('?'))

# squares = {1:1, 2:4, 3:9}
#
#
#
# x = {'a': 2, 'b': 3, 'c': 4}
#
# # for value in x.values():
# #     print(value)
#
# x['d'] = 4
#
# print(x)


# sample = list(range(10))
#
# sample_iterator = iter(sample)
#
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']
#
# zipped_list = dict(zip(list1, list2))
#
# print(zipped_list)



#
# list1 = [1, 'a', 2, 'b', 3, 'c', 4, 'd']
#
# my_iter = iter(list1)
#
# output = dict(zip(my_iter, my_iter))
#
# print(output)

# import json
# sample = '{"name": "kunal", "age": 20, "mob": "123"}'
#
# output = json.loads(sample)
#
# print(output)
# print(type(output))
#
# json_string = json.dumps(output)
# print(json_string)
# print(type(json_string))

# typecast = str(output)
# print(typecast)
# print(type(json_string))
#
# rev_typecast = dict(sample)
# print(rev_typecast)
# print(type(rev_typecast))


# sample.strip("'")
#
# print(type(sample))

'''

0! -> 1
1! -> 1
2! -> 2*1 = 2
3! -> 3*2! = 6
4! -> 4*3! = 24
5! -> 5*4! = 120

n! -> n * (n-1)!

'''
#
#
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n * fact(n-1)
#
#
# print(fact(5))



# def fun():
#     print('Hello')
#     fun()
#
# fun()


# output = lambda x,y:x*y


# output = lambda x,y: x if x>y else y
#
# print(output(7, 3))



# def myfunc(n):
#     return lambda a: a*n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(5))



# filter(my_func, list1)



# def is_even(n):
#     return n%2==0

# num = list(range(11))
#
#
# evens = list(filter(lambda n:n%2==0, num))
#
#
# print(evens)


list1 = list(range(10))

# map(lambda x: abs(x), list1)
#
# map(abs, list1)


# from functools import reduce
#
#
# def add_num(a, b):
#     return a+b
#
#
# output = reduce(add_num, list1)
#
# print(output)
