#Прочитать список строк с клавиатуры. Упорядочить по длине строки.

def solution(strings):
    return len(strings)

strings = []
print("Введите несколько строк. Когда ввод необходимо будет закончить - нажмите Enter.")
string = "Я строка"
while string != "":
    string = input()
    strings.append(string)
strings.remove("")
print(sorted(strings, key=solution))
