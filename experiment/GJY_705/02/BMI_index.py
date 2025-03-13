def BMI_index(height,weight):
    """
    这是一个用于计数BMI的函数
    :param height: 身高
    :param weight: 体重
    :return: BMI值
    """
    return weight / (height*height)

weight = float(input('请输入你的体重(kg):'))
height = float(input('请输入你的身高(M):'))
print(f'你的BMI指数是: {BMI_index(height,weight)}')
