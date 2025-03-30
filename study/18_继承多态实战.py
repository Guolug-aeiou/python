class Employee:
    def __init__(self, name):
        self.name = name

    def salary(self):
        return 0

    # 请补全
    @staticmethod
    def total_salary(employees):
        for temp in employees:
            print(temp)


class Worker(Employee):
    piece_rate = 100  # 单件工资

    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

    def salary(self):
        return self.piece_rate * self.quantity

    def __repr__(self):
        return f'计件工：{self.name}，本月完成工件数：{self.quantity}，工资：{self.salary()}'


class Seller(Employee):
    basic_salary = 3000  # 基本工资
    commision = 20  # 单件提成

    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

    def salary(self):
        return self.commision * self.quantity + self.basic_salary

    def __repr__(self):
        return f'销售员：{self.name}，本月售出商品：{self.quantity}，工资：{self.salary()}'

if __name__ == '__main__':
    employees = []
    employees.append(Worker('张三', 50))
    employees.append(Worker('李四', 75))
    employees.append(Seller('王五', 150))
    Employee.total_salary(employees)
