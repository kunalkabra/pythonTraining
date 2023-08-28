
# # method 1:
# f1 = open('testfile_new.txt', 'a')
# f1.write('this works')
#
# # method 2
# with open('testfile.txt', 'a') as f1:
#     f1.write('this works')

# -------------

# f = open('testfile.txt', 'r')
# f1 = open('testfile_new.txt', 'a')
#
# for data in f:
#     f1.write(data)

# -------------
# # read and write a file
# f = open('testfile.txt', 'a+')
#
# f.write('\nis this working?')
# f.seek(0)
# y = f.readlines()
# print(y)

# -------------
# Regex
import re

my_data = "India is better then Australia"

# output = re.match("India", my_data, re.I)
# print(output)
# print(output.group())

output = re.search('(.*) is (.*?) (.*)', my_data)
print(output.span())

# new_data = "India is better than Australia"
# output = re.search("(.*) is (.*?) (.*)", new_data)
# print(output.group(1))
# print(output.group(2))
# print(output.group(3))


# new_data = "!!! India WON with 49 balls remaining against SRILANKA on 2019 with 330 on score"

# output = re.findall("\d{1,3}", new_data)
# print(output)

# output = re.sub("\W", "_", new_data)
# print(output)

# output = re.split("\W", new_data)
# print(output)

# -------------
#
# import sqlite3
#
# connection = sqlite3.connect('testdb.db')
#
# # -
# query = '''Create table students ('name' text, 'marks' integer)'''
# execution = connection.execute(query)
# print(execution.fetchall())
# connection.commit()
# connection.close()

# query = '''insert into students values ('kunal', 90), ('user1', 85);'''
# execution = connection.execute(query)
# print(execution.fetchall())
# connection.commit()
# connection.close()

# query = '''select * from students;'''
# execution = connection.execute(query)
# print(execution.fetchall())
# connection.commit()
# connection.close()










'''
json -> json
csv -> csv, pandas
pdf -> mypdf
'''

# r -> read
# w -> write, w+
# a -> append, a+

# f = open('text_sample.txt', 'r')
# print(f.read())

# f = open('text_sample.txt', 'w')
# f.write('Test')

# f = open('text_sample.txt', 'r+')
# f.write('\nTest 2 also seems to be working')

# lines = f.readlines()
# f.seek(0)
# f.truncate()
# f.writelines(lines[1:])
#
# f.seek(0)
# f.write('New data')

# f = open('icecream.jpg', 'rb')
# # for i in f:
# #     print(i)
# f2 = open('new_icecream.jpg', 'wb')
# for i in f:
#     f2.write(i)
# #
# # print(f)


# import sqlite3
#
# connection = sqlite3.connect('student_data.db')
#
# # query = '''create table student_info ('name' text, 'marks' integer)'''
#
# # query = '''insert into student_info values ('Kunal', 90), ('user1', 85)'''
#
# query = '''select * from student_info'''
# execution = connection.execute(query)
#
# # for i in execution:
# #     print(i)
#
# print(execution.fetchall())
#
# connection.commit()
# connection.close()

#
# # will need pip3 install
# import pandas as pd
# import numpy as np
#
# from sqlalchemy import create_engine
#
# engine = create_engine('sqlite:///student_data.db')
#
# df = pd.read_sql('Select * from student_info', engine)
# print(df)
#
# dates = pd.date_range("20130101", periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
#
# print(df)




# import re
#
# my_data = "!!! India Won with 49 balls remaining against Srilanka in 2019 with 330 on score"
#
# output = re.findall("\D{1,3}", my_data)
#
# output1 = re.sub("\W", "_", my_data)
#
# output2 = re.split("\W", my_data)
#
# print(output)
# print()
# print(output1)
# print()
# print(output2)



# import numpy as np
#
# a = np.array([1, 2, 3])
#
# b = np.arange(10)
#
# print(b)
# print(b.size)
# print(b.itemsize)

# c = np.array([[1, 2], [3, 4], [5, 6]])
#
# print(c.ndim)
#
# # (rows, columns)
# print(c.shape)
#
# print(c.dtype)



# a = np.arange(20).reshape(4,5)
#
# print(a)

# a = np.array([10, 20, 30, 40])
# b = np.arange(4)
#
# c = a-b
# print(c)
#
# print(b**2)
#
# print(a<35)
#
# b += a
# print(b)


# a = np.arange(5)
#
# print(np.exp(a))
# print(np.sqrt(a))


# a = np.arange(10)**3
# print(a)
#
# # print(a[2])
# # print(a[2:5])
# # print(a[:6:2])
#
# print(a[::-1])
#
# for i in a:
#     print(i**3)


# a = np.arange(4)
# b = a  # shallow copy -> same memory location, same data, different names
# c = a.copy()  # deep copy -> create new instance of the data
# a += 5
# print(a)
# print(b)
# print(c)



'''
1d -> Series
2d -> DataFrame
3d -> Panels (rarely used)
'''

import pandas as pd

# var = list(range(4))
# var_df = pd.Series(var)
#
# print(var_df)

# var = [[1,2,3], [4,5,6,7,8]]
# var_df = pd.DataFrame(var)
#
# print(var_df)



# df = pd.Series(list(range(4)), index=list('abcd'))
# print(df)



# data = {'Country': ['India', 'Pakistan', 'Afghanistan'],
#         'Capital': ['New Delhi', 'Lahore', 'Kabul'],
#         'Population': [1000, 400, 200]}
#
# data_df = pd.DataFrame(data)
#
# print(data_df)
#
# data_df.to_csv('country_data.csv', index=False)



# new_df = pd.read_csv('country_data.csv')
# print(new_df)