initial_balance = 5000
shop_purchase = 1354
lunch = 450
dinner = 1150
final_balance = 1796

# 1. Рассчитаем ожидаемый остаток без чаевых
expected_balance = initial_balance - shop_purchase - lunch - dinner

# 2. Найдем сумму чаевых
tips = expected_balance - final_balance

# 3. Найдем общую сумму счета в кафе
cafe_total = lunch + dinner

# 4. Рассчитаем процент чаевых
tips_percentage = (tips / cafe_total) * 100


print("=== Расчет чаевых Смирнова А.П. ===")
print(f"Начальный баланс: {initial_balance} руб.")
print(f"Покупка в магазине: {shop_purchase} руб.")
print(f"Обед в кафе: {lunch} руб.")
print(f"Ужин в кафе: {dinner} руб.")
print(f"Остаток на счету: {final_balance} руб.")
print()
print(f"Ожидаемый остаток без чаевых: {expected_balance} руб.")
print(f"Сумма чаевых: {tips} руб.")
print(f"Общий счет в кафе: {cafe_total} руб.")
print(f"Процент чаевых: {tips_percentage:.2f}%")


print("\n=== Проверка ===")
total_spent = initial_balance - final_balance
calculated_spent = shop_purchase + lunch + dinner + tips
print(f"Всего потрачено: {total_spent} руб.")
print(f"Расчетные траты: {calculated_spent} руб.")
print(f"Расхождения: {abs(total_spent - calculated_spent)} руб.")