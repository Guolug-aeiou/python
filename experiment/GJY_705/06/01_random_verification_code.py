import random


def verifycode_code():
    code = ''
    for _ in range(6):
        state = random.randint(1, 3)
        if state == 1:
            # 大写字母
            code += chr(random.randint(65, 90))
        elif state == 2:
            # 小写字母
            code += chr(random.randint(97, 122))
        else:
            # 数字
            code += str(random.randint(0, 9))
    return code


if __name__ == '__main__':
    print("生成的验证码：", verifycode_code())
