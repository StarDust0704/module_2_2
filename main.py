# module_2_2
print("Введите чмсло:" )
# Вводим три числа
first = int(input())
second = int(input())
third = int(input())

# Условие проверки количества одинаковых чисел
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)









