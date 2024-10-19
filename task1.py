def convert(currency, course):
    equivalent = currency / course
    return equivalent
try:
    currency = float(input("Введите кол-во валюты: "))
    course = float(input("Введите курс: "))
    if currency < 0:
        raise Exception("Число должно быть не меньше 0")
    elif course <= 0:
        raise ZeroDivisionError("Курс должен быть больше нуля")
except (ValueError, Exception, ZeroDivisionError):
    print("Полечи голову, если денег хватит")
else:
    print(f"Результат: {convert(currency, course)}")
