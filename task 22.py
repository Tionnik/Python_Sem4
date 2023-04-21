
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#    Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#    Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#    m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."""

list1= [4, 2, 5, 8, 3, 7, 14, 3, 24, 11]
list2= [2, 17, 13, 9, 11, 8, 6, 10, 3]
list_end=[]                                             
for i in list1:
    for j in list2:
        if i==j:                                            # Проверяем равенство элементов в массиве
            list_end.insert(0,i)                            # Добавляем новый элемент в начало итогового массива
            if len(list_end)>1:                             # Проверяем совпадений больше одного или нет. 
                for k in range(1, len(list_end)):
                    if list_end[k-1]==list_end[k]:          # Проверяем есть ли такой элемент в итоговом массиве
                        list_end.pop(k-1)                   # Как только находим два одинаковых элементов, один из них исключаем
                        break                               # И переходим к поиску нового одинакового элемента
                    elif i>list_end[k]:                     # Если внесенный элемент больше последующего, то меняем их местами
                        s=list_end.pop(k-1)
                        list_end.insert(k,s)
                    else:
                        break                               # Как только новый элемент оказывается меньше последующего, переходим к поиску нового одинакового элемента
print(list_end) 

