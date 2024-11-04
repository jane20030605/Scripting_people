def add_record(records: list[dict]) -> None:
    """
    新增人員資料到 records 中。允許使用者連續輸入多筆資料。
    """

    def askAge() -> int:
        """供新增資料使用的 Inner Function(函數中的函數，此函數只可在此使用)"""
        while True:
            try:
                age = int(input("請輸入年齡: "))
                break
            # 例:英文、分數、浮點數
            except ValueError:
                print("年齡請輸入正整數")
                continue
        return age

    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = askAge()
        phone = input("請輸入手機號碼: ")

        # 將單筆人員資料存入字典並追加到紀錄列表中
        record = {'部門': department, '姓名': name, '年齡': age, '手機': phone}
        records.append(record)

        cont = input("是否繼續新增資料? (y/n): ").lower()
        if cont == 'n':
            break


def query_record(records: list[dict]) -> None:
    """
    查詢並顯示符合輸入姓名的資料。
    """
    name = input("請輸入要查詢的姓名: ")
    found = False
    for record in records:
        if record['姓名'] == name:
            found = True
            print("\n--- 查詢結果 ---")
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<10}")
            print("-" * 40)
            print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<10}")
            break
    if not found:
        print("查無此人。")


def modify_record(records: list[dict]) -> None:
    """
    修改指定姓名的資料內容。
    """
    name = input("請輸入要修改的姓名: ")
    found = False
    for record in records:
        if record['姓名'] == name:
            found = True
            print("當前資料:")
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<10}")
            print("-" * 40)
            print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<10}")

            print("\n1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機")
            option = int(input("請選擇要修改的欄位: "))
            if option == 1:
                record['部門'] = input("請輸入新的部門: ")
            elif option == 2:
                record['姓名'] = input("請輸入新的姓名: ")
            elif option == 3:
                record['年齡'] = int(input("請輸入新的年齡: "))
            elif option == 4:
                record['手機'] = input("請輸入新的手機號碼: ")

            print("\n--- 更新後的資料 ---")
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<10}")
            print("-" * 40)
            print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<10}")
            break
    if not found:
        print("查無此人。")


def delete_record(records: list[dict]) -> None:
    """
    刪除指定姓名的資料。
    """
    name = input("請輸入要刪除的姓名: ")
    found = False
    for record in records:
        if record['姓名'] == name:
            found = True
            confirm = input(f"確定要刪除 {record['姓名']} 的資料嗎? (y/n): ").lower()
            if confirm == 'y':
                records.remove(record)
                print(f"{record['姓名']} 的資料已刪除。")
                print("\n--- 剩餘的所有資料 ---")
                show_all_records(records)
            break
    if not found:
        print("查無此人。")


def show_all_records(records: list[dict]) -> None:
    """
    顯示所有人事資料，並按照欄位對齊格式化輸出。
    """
    if not records:
        print("目前沒有任何資料。")
    else:
        # 表頭
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<10}")
        print("-" * 40)
        for record in records:
            print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<10}")


def display_menu1() -> None:
    """選單寫法1"""
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("-" * 24)


def display_menu2() -> None:
    """選單寫法2"""
    menuitem = ["新增資料", "查詢資料", "修改資料", "刪除資料", "顯示所有資料", "退出系統"]
    print("\n--- 人事資料管理系統 ---")
    for i in range(len(menuitem)):
        print(f"{i + 1}. {menuitem[i]}")
    print("-" * 24)


records = []
while True:
    # display_menu1()
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("-" * 24)

    option = input("請選擇功能: ")

    if option == '1':
        add_record(records)
    elif option == '2':
        query_record(records)
    elif option == '3':
        modify_record(records)
    elif option == '4':
        delete_record(records)
    elif option == '5':
        show_all_records(records)
    elif option == '6':
        print("系統已退出。")
        break
    else:
        print("無效的選項，請重新選擇。")

    # (可以比較list/class/option....)
    # match option:
    #     case '1':
    #         add_record(records)
    #     case '2':
    #         query_record(records)
    #     case '3':
    #         modify_record(records)
    #     case '4':
    #         delete_record(records)
    #     case '5':
    #         show_all_records(records)
    #     case '6':
    #         print("系統已退出。")
    #         break
    #     case _:
    #         print("無效的選項，請重新選擇。")
