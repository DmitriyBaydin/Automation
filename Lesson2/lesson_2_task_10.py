def bank(X, Y):
    rate = 0.10
    sum_after_Y_years = X * (1 + rate) ** Y
    return sum_after_Y_years


X = int(input("Сколько денег: "))
Y = int(input("Количество лет: "))
result = bank(X, Y)
print(result)
