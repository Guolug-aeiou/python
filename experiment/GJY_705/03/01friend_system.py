def friend_system():
   friends = ['1', '2', '3', '4', '5', '6']
   while True:
       display()
       flag = input('请输入您的选项：')
       if flag == '1':
           add_name = input('请输入你要添加的好友：')
           friends.append(add_name)
           print(f'好友-{add_name}-添加成功！')
       elif flag == '2':
           delete_name = input('请输入你要删除的好友：')
           friends.remove(delete_name)
           print(f'好友-{delete_name}-删除成功！')
       elif flag == '3':
           update_name = input('请输入你要修改的好友：')
           try:
               new_name = input('输入新的名称：')
               friends[friends.index(update_name)] = new_name
               print(f'好友-<{update_name}->{friends[friends.index(new_name)]}>-修改成功！')
           except Exception as e:
               print('输入的好友不在！')
       elif flag == '4':
           count = 1
           print('序号\t |\t姓名')
           for i in friends:
               print(f' {count} \t |\t {i}')
               count += 1
       elif flag == '5':
           print('已退出，感谢使用！')
           break
       else:
           print('输入的选项不存在！')


def display():
   print('---欢迎使用好友系统---')
   print('1:添加好友')
   print('2:删除好友')
   print('3:修改好友')
   print('4:展示好友')
   print('5:退出')
   print('-' * 20)


if __name__ == '__main__':
   friend_system()









