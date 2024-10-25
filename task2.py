menu_ = {"Кофе": 50, "Гамбургер": 200, "Кола": 80, "Чай": 50, "Чизбургер": 225, "Двойной чизбургер": 275, "Наггетсы": 300, "Кетчуп": 100, "Сырный соус": 150}
products = {}
user_info = {}
errors = []
print("Меню кафе:")
for key, value in menu_.items():
    print(f'{key}: {value}')
print()
user_name = input("Введите свое имя: ")
user_info["Имя"] = user_name
while True:
    user_input = input("Выберите продукт (или 'стоп' для завершения): ")
    if user_input == 'стоп':
        break
    else:
        try:
            user_count = int(input(f'Сколько {user_input} вы хотите взять? '))
            if user_count < 1:
                raise Exception("у пользователя проблемы с головой")
            products[user_input] = user_count
        except (ValueError, Exception):
            errors.append("Пользователь ввел некорректное кол-во продуктов")
            print("Вы ввели некорректное кол-во продуктов")

type_of_pay = input("Выберите тип оплаты (наличные/безнал): ")
summ = 0
for key in products.keys():
    try:
        summ += menu_[key]
    except KeyError:
        errors.append("Пользователь заказал несуществующий продукт")
        print("Вы заказали несуществующий продукт")
        break
print(f"Итого к оплате: {summ}")
if type_of_pay not in ["наличные", "безнал"]:
    errors.append("Пользователь ввел неверный тип оплаты")
    print("Вы ввели неверный тип оплаты")
elif type_of_pay == "наличные":
    try:
        user_summ = int(input("Внесите сумму: "))
        if user_summ < summ:
            raise Exception()
    except (ValueError, Exception):
        errors.append("Пользователь некорректно внес сумму")
        print("Вы некорректно внесли сумму")
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
if errors == []:
    check(menu_, products, summ, user_summ)
    user_info["Заказ"] = products
    user_info["Сумма оплаты"] = summ
    user_info["Тип оплаты"] = type_of_pay
    user_info["Внес"] = user_summ
    user_info["Сдача"] = user_summ - summ
else:
    user_info["Ошибки"] = errors
with open("users.txt", 'a', encoding='utf-8') as file:
    for key, value in user_info.items():
        file.write(f"{key}: {value}\n")

