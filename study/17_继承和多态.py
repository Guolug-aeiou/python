class Person:
    """
    person 类
    """

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show_old(self):
        print(self.name, self.age, self.sex)

    def display(self):
        print(self.name, self.age, self.sex)


class Student(Person):
    """
    student 类
    """

    def __init__(self, name, age, sex):
        # 继承父类的init方法
        super().__init__(name, age, sex)

    def display(self):
        print(self.name, self.age, self.sex, 1)


person = Person(1, 2, 3)
person.display()
student = Student(1, 2, 3)
# 调用重写父类的方法
student.display()
# 调用继承父类的方法
student.show_old()


class Animal:
    def speak(self):
        print('动物在叫')


class Dog(Animal):
    def speak(self):
        print('狗在叫')


class Cat(Animal):
    def speak(self):
        print('猫在叫')


# 实例化 cat 类
cat = Cat()
# 实例化 dog 类
dog = Dog()
# 调用重写后的方法
cat.shut()
# 调用重写后的方法
dog.shut()
