# Day 2 作业：班级成绩统计器
scores = [85, 92, 78, 90, 66, 88, 73]
print("人数" + str(len(scores)))
print("最高分" + str(max(scores)))
print("最低分" + str(min(scores)))
print("平均分" + str(round(sum(scores)/len(scores))))
count = 0
for x in scores:      # 逐个取出列表里的元素
    if x < 60:        # 判断条件
        count = count + 1   # 计数加一（等价于 count += 1）
print("不及格人数" + str(count))