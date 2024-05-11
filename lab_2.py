import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика
from functools import reduce

# 1.	Используя функцию map() переписать функцию
items = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def sqr(i):
    return i**2
squared=list(map(sqr,items))
print(squared)


# 2.	Используйте функцию reduce() и перепишите код
reducer = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
fact = reduce(lambda x, y: x*y, reducer)
print(fact)

# 4.	Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
z=list(zip(x,y))
print(z)
# 5.	Используйте функцию zip() чтобы преобразовать код:

name_model = [
    'A7',
    'X5',
    'Tugela',
    'Polo',
    'Laguna',
    'Octavia',
]

name_brand = [
    'Audi',
    'BMW',
    'Geely',
    'VW',
    'Renault',
    'Skoda',
]

# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])

for name, number in zip(name_brand, name_model):
	print(name, '-', number)





# 6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filter_odd_num(numbers):
    if(numbers % 2) == 0:
        return False
    else:
        return True

out_filter = filter(filter_odd_num, numbers)

print("Отредактированный список: ", list(out_filter))





def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

def ShakerSort(nums):          # сортировка шейкерная
    length = len(nums)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):

        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (nums[i] > nums[i + 1]):
                # обмен элементов
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break

        swapped = False

        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (nums[i] > nums[i + 1]):
                # обмен элементов
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        start_index = start_index + 1

def SelectSort(C):       # сортировка выбором
    for i in range(len(C)-1):
        m=i
        for j in range(len(C)):
            if C[j] < C[m]:
                k = C[m]
                C[m] = C[j]
                C[j] = k

def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Пузырьковая", "Быстрая", "Шейкерная", "Выбором"])
x=[]
y1=[]
y2=[]
y3 = []
y4=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))


    B = A.copy()
    C = A.copy()
    nums = A.copy()


    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    SelectSort(C)
    t6 = datetime.datetime.now()
    y4.append((t6 - t5).total_seconds())
    print("Выбором " + str(N) + "   заняла   " + str((t6 - t5).total_seconds())  + "c" )

    t7 = datetime.datetime.now()
    ShakerSort(nums)
    t8 = datetime.datetime.now()
    y3.append((t8 - t7).total_seconds())
    print("Шейкерная" + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds()), str((t8-t7).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "yellow")
plt.plot(x,y4, "#676767")
plt.show()