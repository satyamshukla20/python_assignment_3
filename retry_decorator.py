import time

def solve(**kwargs):
    def fun1(fun):
        num = kwargs['number']
        interval = kwargs['interval']

        def fun2(*args, **kwargs):
            for i in range(num):
                fun(*args, **kwargs)
                time.sleep(interval)
        return fun2 
    return fun1

@solve(number=3, interval = 1)
def ans(task):
    print(task)

ans("this is the text to be printed")