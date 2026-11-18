# Order.py

from Menu import menu

# لیست سفارش‌ها؛ هر سفارش یک دیکشنری است
orders = []


def add_order():
    """دریافت نام محصول و تعداد از کاربر و ذخیره سفارش"""
    name = input("نام محصول را وارد کنید: ").strip().lower()

    if name not in menu:
        print("❌ این محصول در منوی کافه وجود ندارد!")
        return

    try:
        quantity = int(input("تعداد را وارد کنید: "))
        if quantity <= 0:
            print("❌ تعداد باید بزرگ‌تر از صفر باشد!")
            return
    except ValueError:
        print("❌ لطفاً یک عدد صحیح وارد کنید!")
        return

    orders.append({
        "name": name,
        "price": menu[name],
        "quantity": quantity
    })
    print(f"✅ سفارش «{quantity} عدد {name}» با موفقیت ثبت شد.")


def show_orders():
    """نمایش تمام سفارش‌های ثبت‌شده"""
    if not orders:
        print("⚠️  هنوز هیچ سفارشی ثبت نشده است.")
        return

    print("\n========== سفارش‌های ثبت‌شده ==========")
    for i, order in enumerate(orders, start=1):
        print(f"{i}. {order['name']:<10} | "
              f"قیمت واحد: {order['price']:,} | "
              f"تعداد: {order['quantity']}")
    print("=" * 40)