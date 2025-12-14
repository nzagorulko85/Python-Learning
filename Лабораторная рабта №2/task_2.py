salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
mn_cptl = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(1,months+1):
    mn_cptl = mn_cptl + spend - salary
    spend = spend + spend * increase
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(mn_cptl))
