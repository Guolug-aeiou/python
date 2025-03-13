def generate(basics):
    """
    生成密码算法函数
    :param basics: 基础密码
    :return: 加密后密码
    """
    list1 = []
    list1.extend(basics)
    count = 0
    password = ''
    for temp in list1:
        if count % 2 != 0:
            password += temp
        count += 1
    password = password[len(password)::-1]
    if len(password) < 6:
        return password + str(len(basics))
    else:
        return password[0:6] + str(len(basics))
def verify(sPassword):
    """
    验证加密密码是否正确
    :param sPassword: 加密后的密码
    :return: 是否正确
    """
    if generate(sBasics) == sPassword:
        print('密码验证成功!')
    else :
        print('密码验证失败,请重试!')
# 程序主入口
sBasics = input('请输入基础字符串:')
print(f'生成的密码为: {generate(sBasics)}')
sPassword = input('请输入要验证的密码:')
verify(sPassword)