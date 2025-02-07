import re
from termcolor import colored, cprint

print(colored("1 задача (По списку 3)","light_red") + "- Дана строка. Необходимо найти общее количество русских символов.")
print(colored("2 задача (По списку 8)","light_red") + "- Дана строка. Необходимо найти все используемые в ней строчные символы латиницы.")
print(colored("3 задача (По списку 16)","light_red") + "- Дана строка. Необходимо найти минимальное из имеющихся в ней целых чисел.")

request = int(input("Решение какой задачи вам необходимо? Введите номер нужной задачи: "))

if request == 1:
    def solution(sentence):
        pattern = r'[А-ЯЁа-яё]'
        rus = re.findall(pattern, sentence)
        return rus
    text = "Смотря какой fabric, смотря сколько details в этом пиджаке. Может price от 220, самый дорогой 380 $."
    print(text)
    print(solution(text))
    print(len(solution(text)))

elif request == 2:
     def solution(sentence):
        pattern = r'[a-z]'
        lowEng = re.findall(pattern, sentence)
        return lowEng
     text = "Это русские а - ааааа. A vot eti ne ochen' - aaaaaaAAAAAA."
     print(text)
     print(solution(text))

elif request == 3:
    def solution(sentence):
        pattern = r'-?\d+'
        numbers = re.findall(pattern, sentence)
        integers = [int(num) for num in numbers]
        if integers:
            return min(integers) 
        else:
            return None
    sentence = "Есть числа - 0.5, 4, 10, 1"
    print(solution(sentence))