def address_book():
   number_person = {'李四': ['13411111111', 'li4@qq.com']}
   while True:
       display()
       flag = input('请输入功能：')
       if flag == '1':
           name = input('请输入姓名：')
           number = input('请输入手机号：')
           email = input('请输入邮箱：')
           number_person[name] = [number, email]
       elif flag == '2':
           for i in number_person.items():
               print('--*' * 6)
               print(f'姓名：{i[0]}')
               print(f'电话：{i[1][0]}')
               print(f'邮箱：{i[1][1]}')
               print('--*' * 6)
       elif flag == '3':
           name = input("请输入要删除的联系人姓名：")
           try:
               number_person.pop(name)
           except KeyError as e:
               print(f'删除的联系人{e}不存在！')
       elif flag == '4':
           try:
               name = input("请输入要查找的联系人姓名：")
               for i in number_person.items():
                   if i[0] == name:
                       print('--*' * 6)
                       print(f'姓名：{name}')
                       print(f'电话：{number_person[name][0]}')
                       print(f'邮箱：{number_person[name][1]}')
                       print('--*' * 6)
           except KeyError as e:
               print(f'查找的联系人{e}不存在！')
       elif flag == '5':
           print('已退出，感谢使用！')
       else:
           print('输入的选项不存在！')


def display():
   print('=' * 20)
   print('欢迎使用通讯录')
   print('1 添加联系人')
   print('2 查看通讯录')
   print('3 删除联系人')
   print('4 查找联系人')
   print('5 退出')
   print('=' * 20)


if __name__ == '__main__':
   address_book()









