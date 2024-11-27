salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
dolg = 0  #для хранения нехватки зп за каждый месяц
podushka = 0  # это долг плюс зп за весь период

for monthss in range(months): # перебор всех месяцев для переменной в диапазоне 10
    routine = spend - salary #неизменный ежемесячный долг

    if routine > 0:
        dolg += routine #
    spend *= (1 + increase) #это ежемесячная инфляция

podushka = round(dolg)
#     # podushka2 = (spend + (spend * increase)) - salary
#     # podushka3 = ((spend + (spend * increase)) * increase) + spend - salary
# # TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
#
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",podushka)


