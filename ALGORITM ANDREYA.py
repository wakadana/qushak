import math

while True:
    try:
        a = float(input("Введите длину первого катета (или 'q' для выхода): "))
        if a == 'q':
            break
        # Добавляем проверку a < 0
        if a < 0:
            raise ValueError("Длина первого катета не может быть отрицательной")
        b = float(input("Введите длину второго катета: "))
        if b < 0:
            raise ValueError("Длина второго катета не может быть отрицательной")
        c = math.sqrt(a**2 + b**2)
        P = a + b + c
        S = 0.5 * a * b
        print("Периметр:", P)
        print("Площадь:", S)
    except ValueError as e:
        print("Ошибка ввода:", e)