# Пузырьком, сравнивает с соседним и меняет местами или не меняет, до тех пор, пока за веь цикл ничего не поменят. Это с помощью переменной.

arr = [3, 6, 2, 8, 7, 5, 1, 9]

def fun(list):
    result = list
    Stop = True
    while Stop == True:
        Stop = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                var = list[i+1]
                list[i+1] = list[i]
                list[i] = var       
                Stop = True
        
    return result

print (fun(arr))