menu_ = {"Кофе": 50, "Гамбургер": 200, "Кола": 80, "Чай": 50, "Чизбургер": 225, "Двойной чизбургер": 275, "Наггетсы": 300, "Кетчуп": 100, "Сырный соус": 150}
products = {}
print("Меню кафе:")
for key, value in menu_.items():
    print(f'{key}: {value}')
print()
while True:
    user_input = input("Выберите продукт (или 'стоп' для завершения): ")
    if user_input == 'стоп':
        break
    else:
        user_count = input(f'Сколько {user_input} вы хотите взять? ')
        products[user_input] = user_count
type_of_pay = input("Выберите тип оплаты (наличные/безнал): ")
summ = 0
for key in products.keys():
    summ += menu_[key]
print(f"Итого к оплате: {summ}")
if type_of_pay == "наличные":
    user_summ = int(input("Внесите сумму: "))
else:
    user_summ = summ

def check_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "="*30)
        func(*args, **kwargs)
        print("="*30 + "\n")
    return wrapper
@check_decorator
def check(menu_, products, summ, user_summ):
    print("Ваш чек:")
    for key, value in products.items():
        print(f"{key}: {menu_[key]} руб. X {value} шт.")
    print()
    print(f"Итого к оплате: {summ}")
    print(f"Внесено: {user_summ}")
    print(f"Сдача: {user_summ - summ}")
check(menu_, products, summ, user_summ)
