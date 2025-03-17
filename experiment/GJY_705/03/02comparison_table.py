def comparison_table():
    while True:
        uppercase_numbers = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')
        num = int(input('输入 0 ~ 9 其中一个数字：'))

        if num >= 0 and num <= 9:
            print(f'{num} 的中文数字为：{uppercase_numbers[num]}')
        else:
            print('输入错误，请重新输入 0 ~ 9 之间的值！')


if __name__ == '__main__':
    comparison_table()
