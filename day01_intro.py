# 这是我的第一个 Python 程序：个人信息卡片生成器

name = input("你叫什么名字？")
age = input("你几岁了？")
city = input("你在哪个城市？")
target_job = input("你的目标岗位是什么")
age_next_year = int(age) + 1
years_to_30 = abs(30-int(age))
print("=" * 30)
print("        学习名片v2")
print("=" * 30)
print("姓名：" + name)
print("城市：" + city)
print("目标岗位：" + target_job)
print("距30岁还有 " + str(years_to_30) + " 年")
if int(age)  > 60:
    print("终身学习，佩服！")
print("=" * 30)
