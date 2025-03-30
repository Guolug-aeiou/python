# 基本装饰器之处理不带参数函数
import time
from functools import wraps


def my_decorator(func):
    def wrapper():
        print("begin!!")
        func()
        print("over!!")
    return wrapper

# 基本装饰器之处理带参数函数
def my_decorator_is_have_args(func):
    def wrapper(*args,**kwargs):
        print("begin!!!")
        result = func(*args,**kwargs)
        print("over!!!")
        return result
    return wrapper


@my_decorator
def test_decorator():
    print('装饰器')


test_decorator()

# 将装饰器设置为可取消，使用 functools 模块的 wraps 函数，这也是一个装饰器，将其放在 wrapper 函数上，用来存放未装饰的函数，然后在调用时引用__wrapped__
def my_decorator_is_choose(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'{time.time()}Begin!!!')
        result = func(*args,**kwargs)
        print(f'{time.time()}Over!!!')
        return result
    return wrapper

@my_decorator_is_have_args
def add1(num1,num2):
    return num1+num2
add1(1,2)

@my_decorator_is_choose
def add(num1,num2):
    return num1+num2

print('='*20)
# 正常使用装饰器
print(add(1,2))
print('='*20)
# 不使用装饰器
print(add.__wrapped__(1,2))


