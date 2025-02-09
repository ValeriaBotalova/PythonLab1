from termcolor import colored, cprint
import random
print(colored("Отсортировать строки в указанном порядке:", "red"))
print(colored("1 задача (По списку 3)","light_red") + "- Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу глобальным максимумом.")
print(colored("2 задача (По списку 15)","light_red") + "- Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу локальным минимумом")
print(colored("3 задача (По списку 27)","light_red") + "- Дан целочисленный массив. Необходимо осуществить циклический сдвиг элементов массива влево на одну позицию")
print(colored("4 задача (По списку 39)","light_red") + "- Дан целочисленный массив. Необходимо вывести вначале его элементы с четными индексами, а затем – с нечетными.")
print(colored("5 задача (По списку 51)","light_red") + "-Для введенного списка построить два списка L1 и L2, где элементы L1 это неповторяющиеся элементы исходного списка, а элемент списка L2 с номером i показывает, сколько раз элемент списка L1 с таким номером повторяется в исходном.")
print("----------------------------------------------")
request = int(input("Решение какой задачи вам необходимо? Введите номер нужной задачи: "))
print("----------------------------------------------")
if request == 1:
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
        if array[index] == max(array):
            message = f"Элемент по индексу {index} (а именно {array[index]}) является глобальным максимумом."
        else:
            message = f"Элемент по индексу {index} (а именно {array[index]}) не является глобальным максимумом."
        return message
    print(solution(array,index))
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