from termcolor import colored, cprint
import random

print(colored("1 задача (По списку 3)","light_red") + "- Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу глобальным максимумом.")
print(colored("2 задача (По списку 15)","light_red") + "- Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу локальным минимумом.")
print(colored("3 задача (По списку 27)","light_red") + "- Дан целочисленный массив. Необходимо осуществить циклический сдвиг элементов массива влево на одну позицию.")
print(colored("4 задача(По списку 39)","light_red") + " Дан целочисленный массив. Необходимо вывести вначале его элементы с четными индексами, а затем – с нечетными.")
print(colored("5 задача(По списку 51)","light_red") + " Для введенного списка построить два списка L1 и L2, где элементы L1 это неповторяющиеся элементы исходного списка, а элемент списка L2   c номером i показывает, сколько раз элемент списка L1 с таким номером повторяется в исходном.")

print("----------------------------------------------")
request = int(input("Решение какой задачи вам необходимо? Введите номер нужной задачи: "))
print("----------------------------------------------")


#Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу глобальным максимумом.
if request == 1:
    def generateArray(length):
        array = []
        for i in range(length):
            array.append(random.randint(0, 100))
        return array

    length = int(input("Введите длину массива: "))
    array = generateArray(length)
    print(array)

    index = random.randint(0, length - 1)

    def solution(array, index):
        message = ""
        if array[index] == max(array):
            message = f"Элемент по индексу {index} (а именно {array[index]}) является локальным максимумом."
        else:
            message = f"Элемент по индексу {index} (а именно {array[index]}) не является локальным максимумом."
        return message

    print(solution(array, index))

#Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу локальным минимумом.

if request == 2:
    def generateArray(length):
        array = []
        for i in range(length):
             array.append(random.randint(0, 100))
        return array
    length = int(input("Введите длину массива: "))
    array = generateArray(length)
    print(array)
    index = random.randint(0,length - 1)
    def solution(array, index):
        message = ""
        if index == 0:
            if array[index] < array[index+1]:
                message = f"Элемент по индексу {index} (а именно {array[index]}) является локальным минимумом."
            else:
                message = f"Элемент по индексу {index} (а именно {array[index]}) не является локальным минимумом."
        if index == len(array) - 1:
            if array[index] < array[index-1]:
                message = f"Элемент по индексу {index} (а именно {array[index]}) является локальным минимумом."
            else:
                message = f"Элемент по индексу {index} (а именно {array[index]}) не является локальным минимумом."
        else: 
            if (array[index] < array[index+1]) and (array[index] < array[index-1]):
                message = f"Элемент по индексу {index} (а именно {array[index]}) является локальным минимумом."
            else:
                message = f"Элемент по индексу {index} (а именно {array[index]}) не является локальным минимумом."
        return message
    print(solution(array,index))

#Дан целочисленный массив. Необходимо осуществить циклический сдвиг элементов массива влево на одну позицию.
if request == 3:
    def generateArray(length):
        array = []
        for i in range(length):
             array.append(random.randint(0, 100))
        return array
    length = int(input("Введите длину массива: "))
    array = generateArray(length)
    print(array)
    def solution(array):
        if len(array) == 0:
            return array
        return array[1:] + [array[0]]
    print(solution(array))

#Дан целочисленный массив. Необходимо вывести вначале его элементы с четными индексами, а затем – с нечетными.
if request == 4:
    def generateArray(length):
        array = []
        for i in range(length):
             array.append(random.randint(0, 100))
        return array
    length = int(input("Введите длину массива: "))
    array = generateArray(length)
    print(array)
    print("Это элементы с четным индексом - ", *array[::2])
    print("Это элементы с нечетным индексом - ", *array[1::2])

#Для введенного списка построить два списка L1 и L2, где элементы L1 это неповторяющиеся элементы исходного списка, а элемент списка L2   c номером i показывает, сколько раз элемент списка L1 с таким номером повторяется в исходном.
if request == 5:
    list1 = []
    print("Введите элементы списка. Когда ввод необходимо будет закончить - нажмите Enter.")
    string = "Я элемент"
    while string != "":
        string = input()
        list1.append(string)
    list1.remove("")
    print(list1)

    def solution(tList):
        L1 = set(tList)
        L2 = [tList.count(i) for i in L1]
        return L1,L2
    print("Список уникальных элементов, список количества повторений.")
    print(solution(list1))

        

        
    