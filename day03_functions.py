# Day 3 作业：成绩统计器 2.0（函数版）

def analyze(scores):
    result = {}
    result["人数"] = len(scores)
    result["最高分"] = max(scores)
    result["最低分"] = min(scores)
    result["平均分"] = round(sum(scores) / len(scores), 2)
    count = 0
    for x in scores:
        if x < 60:
            count = count + 1
    result["不及格人数"] = count
    return result

def main():
    raw = input("请输入成绩（逗号分隔）：")
    parts = raw.split(",")
    scores = []
    for p in parts:
        scores.append(int(p))
    stats = analyze(scores)
    print("*" * 30)
    for key in stats:
        print(key + "：" + str(stats[key]))
    print("+" * 30)

main()