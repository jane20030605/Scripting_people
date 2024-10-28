# 人事資料管理系統
# 匯入所需模組
from tabulate import tabulate

# 初始化人員資料列表
records = []


def add_record():
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機: ")
        # 將輸入資料存入字典
        record = {
            "department": department,
            "name": name,
            "age": age,
            "phone": phone,
        }
        # 將字典放入列表
        records.append(record)

        more = input("是否繼續新增資料？(y/n): ").lower()
        if more != "y":
            break


def query_record():
    search_name = input("請輸入要查詢的姓名: ")
    found = False
    for record in records:
        if record["name"] == search_name:
            print(
                tabulate(
                    [
                        [
                            record["department"],
                            record["name"],
                            record["age"],
                            record["phone"],
                        ]
                    ],
                    headers=["部門", "姓名", "年齡", "手機"],
                    tablefmt="grid",
                )
            )
            found = True
            break
    if not found:
        print("查無此人")


def modify_record():
    modify_name = input("請輸入要修改的姓名: ")
    found = False
    for record in records:
        if record["name"] == modify_name:
            print(
                tabulate(
                    [
                        [
                            record["department"],
                            record["name"],
                            record["age"],
                            record["phone"],
                        ]
                    ],
                    headers=["部門", "姓名", "年齡", "手機"],
                    tablefmt="grid",
                )
            )
            print("請選擇要修改的欄位：")
            print("1. 修改部門")
            print("2. 修改姓名")
            print("3. 修改年齡")
            print("4. 修改手機")
            choice = input("請選擇要修改的欄位: ")
            if choice == "1":
                record["department"] = input("請輸入新的部門: ")
            elif choice == "2":
                record["name"] = input("請輸入新的姓名: ")
            elif choice == "3":
                record["age"] = input("請輸入新的年齡: ")
            elif choice == "4":
                record["phone"] = input("請輸入新的手機: ")
            else:
                print("無效選項")
                return
            print("修改後的資料：")
            print(
                tabulate(
                    [
                        [
                            record["department"],
                            record["name"],
                            record["age"],
                            record["phone"],
                        ]
                    ],
                    headers=["部門", "姓名", "年齡", "手機"],
                    tablefmt="grid",
                )
            )
            found = True
            break
    if not found:
        print("查無此人")


def delete_record():
    delete_name = input("請輸入要刪除的姓名: ")
    found = False
    for record in records:
        if record["name"] == delete_name:
            print(
                tabulate(
                    [
                        [
                            record["department"],
                            record["name"],
                            record["age"],
                            record["phone"],
                        ]
                    ],
                    headers=["部門", "姓名", "年齡", "手機"],
                    tablefmt="grid",
                )
            )
            confirm = input("是否確定刪除？(y/n): ").lower()
            if confirm == "y":
                records.remove(record)
                print("資料已刪除。")
            else:
                print("操作已取消。")
            found = True
            break
    if not found:
        print("查無此人")
    display_records();


def display_records():
    if records:
        print(
            tabulate(
                [[r["department"], r["name"], r["age"], r["phone"]] for r in records],
                headers=["部門", "姓名", "年齡", "手機"],
                tablefmt="grid",
            )
        )
    else:
        print("目前沒有任何資料")


def main():
    while True:
        print("\n--- 人事資料管理系統 ---")
        print("1. 新增資料")
        print("2. 查詢資料")
        print("3. 修改資料")
        print("4. 刪除資料")
        print("5. 顯示所有資料")
        print("6. 退出系統")
        choice = input("請選擇功能(1-6): ")

        if choice == "1":
            add_record()
        elif choice == "2":
            query_record()
        elif choice == "3":
            modify_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            display_records()
        elif choice == "6":
            print("系統已退出。")
            break
        else:
            print("無效選項，請重新選擇。")


# 呼叫主函數執行程式
main()
