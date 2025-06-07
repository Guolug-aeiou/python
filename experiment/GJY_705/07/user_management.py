from pymysql_utils import MySQLUtils


# 打印菜单
def user_menu():
    print("="*20)
    print("用户管理系统")
    print("1. 查看用户")
    print("2. 添加用户")
    print("3. 修改用户")
    print("4. 删除用户")
    print("0. 退出系统")
    print("="*20)


# 查询users表
def show_users(db):
    users = db.execute_query("SELECT id, username, password FROM users")
    if users:
        print("\n------------用户列表------------")
        for user in users:
            print(f"ID: {user[0]}, 用户名: {user[1]}, 密码: {user[2]}")
    else:
        print("暂无用户信息。")


# 添加用户
def add_user(db):
    username = input("请输入用户名：").strip()
    password = input("请输入密码：").strip()
    if not username or not password:
        print("用户名和密码不能为空！")
        return
    affected = db.execute_update(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    if affected > 0:
        print("用户添加成功！")


# 修改用户
def modify_user(db):
    try:
        user_id = int(input("请输入要修改的用户ID："))
    except ValueError:
        print("无效的用户ID！")
        return

    new_username = input("请输入新的用户名：").strip()
    new_password = input("请输入新的密码：").strip()
    if not new_username or not new_password:
        print("用户名和密码不能为空！")
        return

    affected = db.execute_update(
        "UPDATE users SET username=%s, password=%s WHERE id=%s",
        (new_username, new_password, user_id)
    )
    if affected > 0:
        print("用户信息修改成功！")
    else:
        print("未找到用户或数据未更改。")


# 删除用户
def delete_user(db):
    try:
        user_id = int(input("请输入要删除的用户ID："))
    except ValueError:
        print("无效的用户ID！")
        return

    affected = db.execute_update(
        "DELETE FROM users WHERE id=%s",
        (user_id,)
    )
    if affected > 0:
        print("用户删除成功！")
    else:
        print("未找到用户。")


if __name__ == '__main__':
    try:
        db = MySQLUtils(
            host='127.0.0.1',
            user='root',
            password='root',
            database='pymysql'
        )
    except Exception as e:
        print("程序启动失败：无法连接数据库。")
        exit()

    while True:
        user_menu()
        choice = input("请选择操作：").strip()
        if choice == '0':
            db.close()
            print("系统已退出。")
            break
        elif choice == '1':
            show_users(db)
        elif choice == '2':
            add_user(db)
        elif choice == '3':
            modify_user(db)
        elif choice == '4':
            delete_user(db)
        else:
            print("无效的选项，请重新输入！")
