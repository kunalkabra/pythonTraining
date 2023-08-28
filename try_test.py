

def call_print(i):
    print(i)
    raise Exception


for i in range(5):
    try:
        call_print(i)
        print('test this')
    except: continue
