# 学生信息列表
students = [("张三", 20, 85),
            ("李四", 21, 92),
            ("王五", 19, 50),
            ("赵六", 20, 92),
            ("燕七", 22, 53)]

# 1. 按成绩降序、年龄升序排序
sorted_students = sorted(students, key=lambda x: (-x[2], x[1]))
print("按成绩降序、年龄升序排序后的学生信息：")
for student in sorted_students:
    print(student)

# 2. 过滤出不及格的学生（成绩 < 60）
failed_students = list(filter(lambda x: x[2] < 60, students))
print("\n不及格的学生信息：")
for student in failed_students:
    print(student)

# 3. 计算每个学生的成绩与平均分的差值
average_score = sum(student[2] for student in students) / len(students)
score_differences = list(map(lambda x: (x[0], x[2] - average_score), students))
print("\n每个同学的成绩与平均分的差值：")
for name, difference in score_differences:
    print(f"{name}: {difference:.2f}")
