FILENAME = "ledger.txt"


def load_records():
    """从 ledger.txt 读取历史记录，文件不存在时当成空账本"""
    records = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(line.split(","))
    except FileNotFoundError:
        pass  # 文件不存在，就当空账本，不报错
    return records


def append_record(record):
    """把一条记录追加写入 ledger.txt"""
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(",".join(record) + "\n")


def add_record(records):
    kind = input("类型（收入/支出）：").strip()
    if kind not in ("收入", "支出"):
        print("类型必须是 收入 或 支出")
        return
    amount_str = input("金额：").strip()
    try:
        amount = float(amount_str)
    except ValueError:
        print("金额必须是数字")
        return  # 回到菜单
    note = input("备注：").strip()
    record = [kind, f"{amount:g}", note]
    records.append(record)
    append_record(record)
    print("已记一笔")


def show_records(records):
    if not records:
        print("暂无记录")
        return
    for i, r in enumerate(records, 1):
        print(f"{i}. {r[0]} {r[1]}元  备注：{r[2]}")


def show_total(records):
    total = 0.0
    for r in records:
        if r[0] == "收入":
            total += float(r[1])
        elif r[0] == "支出":
            total -= float(r[1])
    print(f"结余（收入 - 支出）：{total:.2f}元")


def main():
    records = load_records()
    print(f"已加载 {len(records)} 条历史记录")
    while True:
        print("\n===== 记账本 =====")
        print("1 记一笔")
        print("2 查看全部记录")
        print("3 统计总额")
        print("q 退出")
        choice = input("请选择：").strip()
        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            show_total(records)
        elif choice == "q":
            print("再见！")
            break
        else:
            print("无效选项，请重新输入")


main()
