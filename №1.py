f = open('№1.txt')
n = int(f.readline()) #считываем количество рядов в кинозале
m = int(f.readline()) # общее количество занятых мест, то есть то, из чего состоит файл
mat = [["." for i in range(n)] for j in range(n)] #создаём матрицу, заполняя ее точками
for i in range(m):
    s = [int(x) for x in f.readline().split()]
    nr = int(s[0]) #номер ряда
    nm = int(s[1]) #номер места
    mat[nr-1][nm-1] = "*" #занятые места заполняем звездочками
vch = 0 #верхняя четверть
nch = 0 #нижняя четверть
pch = 0 #правая четверть
lch = 0 #левая четверть
for i in range(n):     # проходимся по
    for j in range(n):  #      матрице
        if i > j and i < n -1 -j: # условия для левой четверти 
            if mat[i][j] == "*": #если место занято:
                lch += 1    
        if i < j and i > n - 1- j: #условия для правой четверти
            if mat[i][j] == "*": #если место занято:
                pch += 1
        if i > j and i > n -1 -j: #условия для нижней четверти
            if mat[i][j] == "*": #если место занято:
                nch += 1
        if i < j and i < n -1 -j: #условия для верхней четверти
            if mat[i][j] == "*": #если место занято:
                vch += 1
if max(pch,vch,lch,nch) == vch: #используем конструкцию if-elif-else:
    print(1, vch)               #чтобы вывести четверть с минимальным
elif max(pch,vch,lch,nch) == pch: #номером, если их несколько
    print(2, pch)
elif max(pch,vch,lch,nch) == nch:
    print(3, nch)
else:
    print(4, lch)
