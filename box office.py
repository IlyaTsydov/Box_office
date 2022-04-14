n = int(input("Сколько мест вы хотите забронировать? "))
print("Укажите возраст каждого посетителя")
s = 0
for i in range(1, n +1):
    age = int(input("Возраст: "))
    if age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    else:
        price = 1390
    s = s + i
if n > 3:
    f = 0.9
else:
    f = 1
print("Вынь да положь -", n * price * f)