def delete_content(students):
    delete_name = {'姓名': input('请输入你要删除的学生：'), '性别': input('请输入学生性别：')}
    for temp in students:
        if temp['姓名'] == delete_name['姓名'] and temp['性别'] == delete_name['性别']:
            students.remove(temp)
            print(f"学生-{delete_name['姓名']},{delete_name['性别']}-删除成功！")
            break
    else:
        print('学生不存在！')


def add_content(students):
    add_name = {'姓名': input('请输入新学生的姓名：'), '性别': input('请输入新学生的性别：')}
    students.append(add_name)
    print(f'新学生-{add_name['姓名']}-添加成功！')


def update_content(students):
    update_old_name = {'姓名': input('请输入你要修改的学生：'), '性别': input('请输入学生性别：')}
    for index, temp in enumerate(students, start=0):
        if temp['姓名'] == update_old_name['姓名'] and temp['性别'] == update_old_name['性别']:
            update_new_name = {'姓名': input('请输入学生新姓名：'), '性别': input('请输入学生性别：')}
            students[index]['姓名'] = update_new_name['姓名']
            students[index]['性别'] = update_new_name['性别']
            print(f"学生-{update_old_name['姓名']},{update_old_name['性别']}-修改为：")
            print(f"学生-{update_new_name['姓名']},{update_new_name['性别']}-")
            break
    else:
        print('学生不存在！')


def student_content_display(students):
    print('=' * 30)
    print('序号\t姓名\t性别')
    for index, temp in enumerate(students, start=1):
        print(f'{index}\t{temp["姓名"]}\t{temp["性别"]}')


def menu_display():
    print('=' * 30)
    print('学生管理系统')
    print('1:添加学生信息')
    print('2:删除学生信息')
    print('3:修改学生信息')
    print('4:显示所有学生信息')
    print('5:退出')
    print('=' * 30)


def main():
    students = [{'姓名': '张三', '性别': '男'},
                {'姓名': '李四', '性别': '女'}]
    while True:
        # 打印菜单
        menu_display()
        flag = input('请输入您的选项：')
        # 添加
        if flag == '1':
            add_content(students)
        # 删除
        elif flag == '2':
            delete_content(students)
        # 修改
        elif flag == '3':
            update_content(students)
        # 显示
        elif flag == '4':
            student_content_display(students)
        # 退出
        elif flag == '5':
            print('已退出，感谢使用！')
            break
        else:
            print('输入的选项不存在！')


if __name__ == '__main__':
    main()
