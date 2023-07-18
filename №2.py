f = open("№2.txt")#1 шаг - считываем
n = int(f.readline())
rest = [] #список для людей, у которых время пребывания <= 20
for i in range(n): #2 шаг
    s = [int(x) for x in f.readline().split()]
    vr = s[2] - s[1] #находим время нахождения человека в ресторане
    if vr <= 20:
        s[2] = vr #вместо времени ухода оставляем vr
        rest.append(s)
rest.sort()
#print(rest)
rest1 = []
par = []
for i in range(len(rest)):  #3 шаг делаем список списков, то есть список парочек.
    if len(par) == 0:
        par.append(rest[i])
    else:
        if par[-1] == rest[i]:
            par.append(rest[i])
        else:
            if len(par) == 2:
                rest1.append(par)
                par = []
                par.append(rest[i])
            else:
                par = []
                par.append(rest[i])
rest1.append(par)

rest = []
for i in range(len(rest1)):  #4 шаг. нам не нужны дубликаты,так как мы рассматриваем пары, избавимся от них так.
    rest.append(rest1[i][0])    #(это можно было бы сделать в экселе) len(res) - это наш первый ответ
pr = []
k = 1 #количество одновременно ужинающих пар
maxk = 0
for i in range(len(rest)): # 5 шаг 
    if i == 0:
        pr = rest[i]
    else:
        if pr[2]+pr[1] >= rest[i][1]:
            k += 1 #количество одновременно ужинающих пар +1
        else:
            maxk = max(maxk,k)#выбираем максимум, т.к. нам  нужно наибольшее число.
            k = 1
print(len(rest),maxk) #len(rest) - всего пар посетили ресторан за сутки, maxk
