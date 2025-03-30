class Friend:
    def __init__(self,name,phone,email):
        self.name =name
        self.phone=phone
        self.email=email
    def __repr__(self):
        return f"姓名：{self.name}\n电话：{self.phone}\n邮箱：{self.email}"

class FriendList:
    def __init__(self):
        self.list = []

    def add_friend(self, friend):
        self.list.append(friend)

    def remove_friend(self, name):
        count = 0
        flag = False
        for value in self.list:
            if name == value.name:
                self.list.pop(count)
                print(value)
                flag = True
            count +=1
            if flag:
                print("删除成功！")
                break
            
    def show_all_friends(self):
        print(f"{'='*25}")
        for i in self.list:
            print(f"{i}")
            print(f"{'='*25}")


def enum():
    print('--- 好友通信录系统 ---')
    print('1, 查看所有好友')
    print('2, 添加好友')
    print('3, 删除好友')
    print('4, 退出系统')

if __name__ == "__main__":
    # 添加测试数据
    friendlist = FriendList()
    friendlist.add_friend(Friend('张三1','1341121111','guolu1g@qq.com'))
    friendlist.add_friend(Friend('张三2','1341131111','guolu3g@qq.com'))
    friendlist.add_friend(Friend('张三3','134121111','guolu32g@qq.com'))
    while True:
        enum()
        flag = input('请输菜单编号：')
        if flag == "1":
            friendlist.show_all_friends()
        elif flag == "2":
            name = input('请输入要添加的名称：')
            phone = input('请输入要添加的电话：')
            email = input('请输入要添加的邮箱：')
            friendlist.add_friend(Friend(name=name,phone=phone,email=email))
        
        elif flag == "3":
            friendlist.remove_friend(input('请输入要删除的名称：'))
        
        elif flag == "4":
            print('感谢使用本系统！！')
            break
        
        else :
            print('请输入正确的菜单！！！')
