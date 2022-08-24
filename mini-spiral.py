# Заполнение заданного поля цифрами, с еденицы по возврастающей, из центра поля по спирали.

# Создание поля
def creat_field(a: int, b: int) -> list[list[int]]:
    '''Создаем поле которое в дальнейшем будем заполнять цифрами.'''
    field = []
    for row in range(a):
        field.append([])
        for col in range(b):
            field[row].append(0)
        print(field[row])
    return field

# Ищем центр поля
def find_center (field_arg) -> tuple:
    '''Находим центр поля в зависимости от кратности двум, размера поля.'''
    if len(field_arg) % 2 == 0:
        y = len(field_arg) / 2 - 1
    else:
        y = (len(field_arg) - 1) / 2
    if len(field_arg[0]) % 2 == 0:
        z = len(field_arg) / 2 - 1
    else:
        z = (len(field_arg[0]) - 1) / 2
    return (int(y), int(z))

# Задаем логику заполнения
def logica(hod: tuple) -> dict:
    right = (0, 1)
    bottom = (1, 0)
    left = (0, -1)
    top = (-1, 0)

    if hod == right:
        proverka = bottom
        next_hod = bottom
    elif hod == bottom:
        proverka = left
        next_hod = left  
    elif hod == left:
        proverka = top
        next_hod = top
    elif hod == top:   
        proverka = right
        next_hod = right   
    return {"proverka": proverka, "next_hod": next_hod}

def get_proverka(hod: tuple) -> tuple:
    right = (0, 1)
    bottom = (1, 0)
    left = (0, -1)
    top = (-1, 0)

    if hod == right:
        return bottom
    elif hod == bottom:
        return left  
    elif hod == left:
        return top
    elif hod == top:   
        return right

# Заполнение
def do_it(center_arg: tuple, field_arg: list[list[int]]):
    right = (0, 1)
    y = center_arg[0]
    z = center_arg[1]
    field_arg[y][z] = 1
    count = 2

    # Первый ход вправо
    hod = right
    proverka = None

    while count <= len(field_arg) * len(field_arg[0]):
        field_arg[y + hod[0]][z + hod[1]] = count
        y = y + hod[0]
        z = z + hod[1]
        count = count + 1
        proverka = get_proverka(hod)

        if field_arg[y + proverka[0]][z + proverka[1]] == 0:
            hod = logica(hod)["next_hod"]



field = creat_field(7, 7)
center = find_center(field)

print ("\n")
print (center)

do_it(center, field)


# Печатаем результат
print ("\n")   
for i in field:
    print (i)   
        



