import datetime

def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    
    # Рассчитываем возраст в годах
    age = today.year - birth_date.year
    
    # Учитываем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def get_birth_date_info():
    day = int(input("Введите день вашего рождения: "))
    month = int(input("Введите месяц вашего рождения: "))
    year = int(input("Введите год вашего рождения: "))

    day_of_week = get_day_of_week(day, month, year)
    leap_year = is_leap_year(year)
    age = calculate_age(day, month, year)
    
    leap_year_status = "високосный" if leap_year else "не високосный"
    
    print(f"Ваш день рождения: {day}-{month}-{year}, и это был {day_of_week}")
    print(f"Год {year} является {leap_year_status} годом.")
    print(f"Вам сейчас {age} лет.")

get_birth_date_info()