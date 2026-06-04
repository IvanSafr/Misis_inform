strange_list = ["OOOOOhhOOO", "aircraft", 14, 175, 12.3, "navy"]
print(strange_list)

user_unswer = input("Какую половину списка вы хотите удалить? (1 или 2): ")
del_count = len(strange_list) // 2

if user_unswer=="1":

    print("Удаляем первую")
    # Переписать это
    for i in range(del_count):
        pass

elif user_unswer=="2":
    print("Удаляем вторую")
    # И это
    for i in range(del_count):
        pass

#print(strange_list)