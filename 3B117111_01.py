def find_product(products, pid):
    """
    根據 ID 查詢產品資料
    """
    for p in products:
        # 使用 get("id") 安全取值並進行比對
        if p.get("id") == pid:
            return {"success": True, "data": p}
    
    # 如果迴圈跑完都沒找到，回傳失敗
    return {"success": False, "data": None}

def format_price(price):

    return f"${price:,}"

if __name__ == "__main__":
    # 建立題目要求的產品列表
    products = [
        {"id": 1, "name": "Keyboard", "price": 1200},
        {"id": 2, "name": "Mouse", "price": 800},
        {"id": 3, "name": "Monitor", "price": 4500}
    ]

    # --- 測試案例 1：查詢 ID: 1 ---
    print("=== 查詢 ID: 1 ===")
    result1 = find_product(products, 1)
    if result1["success"]:
        p = result1["data"]
        # 呼叫格式化價格函式
        formatted_p = format_price(p["price"])
        print(f"找到產品: {p['name']}, 價格: {formatted_p}")
    else:
        print("=> 查無此產品")

    print() # 空一行，對齊預期畫面

    # --- 測試案例 2：查詢 ID: 99 ---
    print("=== 查詢 ID: 99 ===")
    result2 = find_product(products, 99)
    if result2["success"]:
        p = result2["data"]
        formatted_p = format_price(p["price"])
        print(f"找到產品: {p['name']}, 價格: {formatted_p}")
    else:
        print("=> 查無此產品")