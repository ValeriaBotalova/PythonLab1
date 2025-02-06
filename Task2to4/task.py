import random
from termcolor import colored, cprint

print(colored("1 задача (По списку 3)","light_red") + "- Дана строка в которой слова записаны через пробел. Необходимо перемешать все слова этой строки в случайном порядке.")
print(colored("2 задача (По списку 8)","light_red") + "- Дана строка в которой записаны слова через пробел. Необходимо посчитать количество слов с четным количеством символов.")
print(colored("3 задача (По списку 16)","light_red") + "- Дан массив в котором находятся строки \"белый\", \"синий\" и \"красный\" в случайном порядке. Необходимо упорядочить массив так, чтобы получился российский флаг.")

request = int(input("Решение какой задачи вам необходимо? Введите номер нужной задачи: "))

if request == 1:
    def solution(sentence):
        partition = sentence.split()
        random_times = random.randint(0, 13)
        while random_times > 0:
            frandom_index = random.randint(0, len(partition) - 1)
            srandom_index = random.randint(0, len(partition) - 1)
            if frandom_index != srandom_index:
                partition[frandom_index], partition[srandom_index] = partition[srandom_index], partition[frandom_index]
            random_times -= 1
        return partition

    def smartSolution(sentence):
        partition = sentence.split()
        random.shuffle(partition)
        return partition
    
    sentence = input("Введите предложение: ")
    print("Решение через цикл: ")
    print(solution(sentence))
    print(solution(sentence))
    print("Решение со встроенными функциями: ")
    print(smartSolution(sentence))
    print(smartSolution(sentence))

elif request == 2:

    def solution(sentence):
        allDigit = []
        digit = 0
        evenDigit = 0
        for i in sentence:
            if i != " ":
                digit += 1
            else:
                allDigit.append(digit)
                digit = 0
        allDigit.append(digit)
        for j in allDigit:
            if j%2 == 0:
                evenDigit += 1
        return evenDigit
    
    def smartSolution(sentence):
        words = sentence.split()
        even_count = sum(1 for word in words if len(word) % 2 == 0)
        return even_count
    
    sentence = str(input("Введите предложение: "))
    print("Решение через цикл: ")
    print(solution(sentence))
    print("Решение через встроенные функции: ")
    print(smartSolution(sentence))

elif request == 3:
    futureFlag = ["белый", "синий", "красный"]

    def mixing(sentence):
        random_times = random.randint(0, 13)
        while random_times > 0:
            frandom_index = random.randint(0, len(sentence) - 1)
            srandom_index = random.randint(0, len(sentence) - 1)
            if frandom_index != srandom_index:
                sentence[frandom_index], sentence[srandom_index] = sentence[srandom_index], sentence[frandom_index]
            random_times -= 1
        return sentence

    print("Изначальный массив: ", mixing(futureFlag))

    def solution(sentence):
        colors = {"белый": 0, "синий": 1, "красный": 2}
        sorted_sentence = sorted(sentence, key=lambda x: colors[x])
        return sorted_sentence

    print("Получившийся флаг: ", solution(futureFlag))
            