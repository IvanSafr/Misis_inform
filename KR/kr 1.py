while True:
    in_v = input("Введите высоту и и меньшее основание для прямоугольной трапеции через пробел (целые числа): ")

    try:
        a, h = map(int, in_v.split())

        break
    except Exception as E:
        print("Введите данные корректно\n")



answr = ""
for i in range(h):
    answr += "*"* a
    answr += '\n'
    a+=1

print(f"Искомая трапеция: \n\n{answr}")
