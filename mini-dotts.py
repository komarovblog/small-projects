# Дан список координат, например [(2.03, 1.75), (3.4, 12.7), (6.8,17.2)] 
# Написать функцию, которая находит две ближайшие друг к другу точки.

dotts = [(2.03, 1.75), (3.4, 12.7), (6.8,17.2)]

def fun (dotts):
    d1 = None
    d2 = None
    i = 0
    most_small_distance = None
    for i in range (0, len(dotts)):
        for y in range (i+1, len(dotts)):
            a = abs(dotts[i][0] - dotts[y][0])
            b = abs(dotts[i][1] - dotts[y][1])
            distans = (a**2 + b**2)**0.5
            
            if most_small_distance is None or distans < most_small_distance:
              most_small_distance = distans
              d1 = dotts[i]
              d2 = dotts[y]

    result = {}
    result['otrezok'] = most_small_distance
    result['d1'] = d1
    result['d2'] = d2
    return result

print (fun(dotts))