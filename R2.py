# 5, 9, 10

# 5, В	соревнованиях	по	бегу	принимают	участие	30	спортс
# менов.	Вводя	по	очереди	результаты	участников,	определить,
# сколько	из	них	выполнили	заданный	норматив.
# cnt = 0
# #
# n = int(input("Введите кол-во спортсменов: "))
# norm = float(input("Введите значение норматива: "))
# for i in range(n):
#     res = float(input(f'Введите спортсмена №{i+1}:'))
#
#     if res > norm:
#         print("Не сдал")
#         continue
#
#     cnt += 1
#     print("Сдал")
#
# print(f'Спортсменов, сдавших норматив: {cnt}')
#
# 9.	В	соревнованиях	по	плаванию	на	200	м	участвуют	n
# спортсменов.	Вывести	на	печать	лучший	результат.

# n = int(input('Сколько человек участвует в соревнованиях?: '))
# res_t = dict()
#
# for i in range(n):
#     key, val = map(str, input("Введите фамилию и время через пробел:\n").split())
#     res_t[float(val)] = key
#
# best_res = min(res_t.keys())
# print(f"Лучший результат: {res_t[best_res]} - {best_res} c.")

#  10.	В	группе	учится	n	студентов.	Каждый	получил	на	экза
# менах	по	4	оценки.	Подсчитать	число	студентов,	не	имеющих
# «2»	и	«3».

# n = int(input('Сколько человек учится в группе?: '))
# res_t = dict()
#
# for i in range(n):
#     in_v_lst = list(map(str, input("Введите фамилию и оценки пробел:\n").split()))
#
#     res_t[in_v_lst[0]] = in_v_lst[1:]
#
# cnt = 0
#
# print("\nСписок хороших учеников:\n")
# for k, v in res_t.items():
#     if "2" not in v and "3" not in v:
#         print(f"{k} - {v}")
#         cnt += 1
# print(f"Всего умных студентов: {cnt}")

# Уровень 3


#задача 5
# norm = float(input("Введите значение норматива): "))
# cnt = 0
# while True:
#     in_v = input(f'Введите результат спортсмена (для завершения - end): ')
#     if in_v == 'end':
#         break
#     try:
#         res = float(in_v)
#     except Exception as E:
#         print(E)
#         continue
#
#     if res > norm:
#         print("Не сдал")
#         continue
#
#     cnt += 1
#     print("Сдал")
#
# print(f'Спортсменов, сдавших норматив: {cnt}')


#задача  9
res_t = list()
while True:
    in_val = input("Введите время через пробел (что бы закончить ввод 0): \n")

    if in_val == '0':
        break
    try:
        val = float(in_val)
    except Exception as E:
        print(E)
        continue
    res_t.append(val)

if len(res_t)==0:
    print(0)
else:
    best_res = min(res_t)
    print(f"Лучший результат: {best_res} \n\n\n")


# Задача 10
res_t = dict()

while True:
    in_v = input("Введите фамилию и оценки пробел (для завершения - end):\n")
    if in_v == 'end':
        break

    try:
        in_v_lst = list(map(str, in_v.split()))
        res_t[in_v_lst[0]] = in_v_lst[1:]
    except Exception as E:
        print(E)
        continue

cnt = 0

print("\nСписок хороших учеников:\n")
for k, v in res_t.items():
    if "2" not in v and "3" not in v and len(v)>2:
        print(f"{k} - {v}")
        cnt += 1
print(f"Всего умных студентов: {cnt}")