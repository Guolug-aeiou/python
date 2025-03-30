# 创建一个 A 类
class A:
    pass


# 创建一个 B 类
class B:
    pass


# 实例化对象 A 和 B
a = A()
b = B()


# 创建一个 C 类
class C:
    # 初始化方法
    def __init__(self, age, sex, name):
        # 成员变量
        self.age = age
        self.sex = sex
        self.name = name

    # 常规方法
    def display(self):
        print(self.age, self.sex, self.name)


c = C(24, True, 'guolug')
c.display()


# 创建一个 D 类
class D:
    # 初始化方法
    def __init__(self, age, sex, name):
        # 成员变量
        self.age = age
        self.sex = sex
        self.name = name

    # 魔法方法
    def __str__(self):
        return f'{self.name}是{'男生' if self.sex else '女生'}，今年 {self.age} 岁'

    # 常规方法
    def display(self):
        print(self.__str__())


d = D(24, True, 'guolug')
d.display()


# student 类
class student:
    def __init__(self, name, age, sex):
        # 默认是公开的 public  类内部可，子类可，外部可
        self.name = name
        #  _ 是受保护的 protected  类内部可，子类可，外部不可
        self._age = age
        #  __ 是私有的 private  类内部可，子类不可，外部不可
        self.__sex = sex

    def __str__(self):
        print(self.name, self._age, self.__sex)


st = student(10, 101, 1)


class S:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = S('name', 24)


# s.sex = True

# 静态方法 和 property 装饰器
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # 静态方法
    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    @property
    def perimeter(self):
        """计算周长"""
        if self.is_triangle(self.a, self.b, self.c):
            return self.a + self.b + self.c
        return False

    @property
    def area(self):
        """计算面积"""
        if self.is_triangle(self.a, self.b, self.c):
            p = self.perimeter / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return False

    # 静态方法
    @classmethod
    def is_triangle_class(cls,a, b, c):
        return a + b > c and a + c > b and b + c > a

# 静态方法可以使用 类名.方法() / 示例.方法()
Triangle.is_triangle(3,4,5)
triangle = Triangle(3,4,6)
triangle.is_triangle(3,4,6)
# @property 装饰器 将方法变为属性，在定义属性时需要对传入值进行一些处理时可以使用
print(triangle.perimeter)
print(triangle.area)
# 类方法
t = Triangle.is_triangle_class(1,2,3)
