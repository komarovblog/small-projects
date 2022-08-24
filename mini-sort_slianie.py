# Слияние делит список на две части, сортирует и сливает их. Те две части можно сливать.
# # Сортировка слиянием arr = [1, 6, 3, 2, 7, 7, 8, 6, 9]


def separate(list_arg: list) -> list:
    #Делим на два списка, четные в один нечетные в другой
    new_arr_1 = []
    new_arr_2 = []
    for i in range(len(list_arg)):
        if i % 2 != 0:
            new_arr_1.append(list_arg[i])
        else:
            new_arr_2.append(list_arg[i])

    # Если список больше двух вызываем рекурсию
    if len(new_arr_1) > 2:
        new_arr_1 = separate(new_arr_1)
    if len(new_arr_2) > 2:
        new_arr_2 = separate(new_arr_2)

    # Если список меньше двух объединяем и сортируем пызырьком
    if len(new_arr_1) <= 2 and len(new_arr_2) <= 2:
        z = 0
        new_arr_pusir = []
        new_arr_pusir = new_arr_1 + new_arr_2     
        stop = True
        while stop:
            stop = False
            for i in range(len(new_arr_pusir)-1):
                if new_arr_pusir[i] > new_arr_pusir[i+1]:
                    new_arr_pusir[i], new_arr_pusir[i+1] = new_arr_pusir[i+1], new_arr_pusir[i]
                    stop = True
        return new_arr_pusir

    # Теперь то что вернула рекурсия сортируем слиянием
    a = 0
    b = 0
    result = []
    while True:
        if new_arr_1[a] <= new_arr_2[b]:
            result.append(new_arr_1[a])
            a = a + 1
        else:
            result.append(new_arr_2[b])
            b = b + 1
        if a >= len(new_arr_1):
            result.extend(new_arr_2[b:])
            break          
        if b >= len(new_arr_2):
            result.extend(new_arr_1[a:])
            break
    return result

arr = [1, 6, 3, 2, 7, 7, 8, 6, 9]
print(separate(arr))