#Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.
def solution(x):
    return len(x.split())

strings = []
print("Введите несколько строк. Когда ввод необходимо будет закончить - нажмите Enter.")
string = "Я строка"
while string != "":
    string = input()
    strings.append(string)
strings.remove("")
print(sorted(strings,key=solution))