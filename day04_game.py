import random

def main():
    difficulty = input("难度")# 1. input 让用户选难度，if 判断决定范围上限
    if difficulty == "1":
        upper = 50
    else:
        upper = 100
    secret = random.randint(1, upper)
    count = 0
    while True:        
        guess = int(input("你猜："))
        count += 1
        if guess == secret:
            print("恭喜" + str(count))#打印恭喜 + 次数
            break      #猜中就跳出去
        elif guess > secret:
            print("猜大了")
        else:
            print("猜小了")

main()