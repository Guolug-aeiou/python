def login(userName,password) -> str:
    if userName == 'admin' and password == '123456':
        return '登录成功!'
    else:
        return '您输入的用户名或密码错误!'


