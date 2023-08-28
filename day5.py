# from sqlalchemy import create_engine
# import pandas as pd
# import numpy as np
#
# engine = create_engine('sqlite:///student_data.db')
#
# # student_df = pd.read_sql('select * from student_info;', engine)
# # student_df.to_html()
# # print(student_df)
#
# date_index = pd.date_range('20190101', periods=6)
#
# data_df = pd.DataFrame(np.random.randn(6, 4), index=date_index, columns=list('abcd'))
#
# print(data_df)

import pandas as pd

num = [[1,2,3], [4,5,6,7]]

df = pd.DataFrame(num)
df = df.fillna(0)

df.to_csv('pandas_test.csv')
print(df)



import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(10, 6))

# x = np.arange(6)
# y1 = np.power(x, 2)
# y2 = np.power(x, 3)

#
# x = np.linspace(0, 10, 1000)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y1, label='sin wave')
# plt.plot(x, y2, label='cos wave')
#
# plt.fill_between(x, 0, y1)
# plt.fill_between(x, 0, y2)
#
# plt.grid(linestyle='-', color='red')
#
# plt.legend(loc='upper left')
# plt.xlabel('X-Axis', fontsize=15)
# plt.ylabel('Y-Axis', fontsize=15)
# plt.show()

#
x = list(range(4))
y = [5, 25, 35, 40]

x1 = [2, 4, 6, 8]
y1 = [17, 18, 29, 42]

ax = plt.axes()
ax.set_facecolor('red')

plt.bar(x, y, color='#42B300')
plt.bar(x1, y1, color='blue')

plt.tight_layout()
plt.show()


# import threading
# from time import sleep
#
# def Hello(name, lock):
#     for i in range(50):
#         lock.acquire()
#         print("Hello ", name)
#         lock.release()
#         # sleep(1)
#
#
# # def Hi(name, mob):
# #     for i in range(50):
# #         print(f'Hi {name} mob: {mob}')
# #         # sleep(1)
#
#
# lock = threading.Lock()
# t1 = threading.Thread(target=Hello, args=('Kunal',lock))
# t2 = threading.Thread(target=Hello, args=('User 1',lock))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("This is done!")

