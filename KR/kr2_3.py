def summing(st:str):
    s = 0
    for h in st:
        s += int(h)
    return s

def proisv(st:str):
    s = 1
    for h in st:
        s *= int(h)
    return s


n = int(input('Введите кол-во строк: '))
cnt = 0
str_lst = []
while True:
    if cnt == n:
        break
    in_v = input("Введите строку из 3 цифр (подряд)")

    if len(in_v)!=3 or not in_v.isdigit():
        print('Введите данные корректно')
        continue

    str_lst.append(in_v)
    cnt += 1
print("\n\n")
for el in str_lst:

    print(f"{el}: Сумма: {summing(el)} Произведение: {proisv(el)}")
