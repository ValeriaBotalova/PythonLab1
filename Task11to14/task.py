from termcolor import colored, cprint
from collections import Counter
print(colored("Отсортировать строки в указанном порядке:", "red"))
print(colored("1 задача (По списку 3)","light_red") + "- В порядке увеличения разницы между частотой наиболее часто встречаемого символа в строке и частотой его появления в алфавите.")
print(colored("2 задача (По списку 5)","light_red") + "- В порядке увеличения квадратичного отклонения частоты встречаемости самого часто встречаемого в строке символа от частоты его встречаемости в текстах на этом алфавите.")
print(colored("3 задача (По списку 7)","light_red") + "- В порядке увеличения разницы между количеством сочетаний «гласная-согласная» и «согласная-гласная» в строке.")
print(colored("4 задача (По списку 12)","light_red") + "- В порядке увеличение квадратичного отклонения частоты встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.")
print("----------------------------------------------")
request = int(input("Решение какой задачи вам необходимо? Введите номер нужной задачи: "))
print("----------------------------------------------")
alphabet= {
    'а': 0.07998,'б': 0.01592,'в': 0.04533,
    'г': 0.01687,'д': 0.02977,'е': 0.08483,
    'ё': 0.00013,'ж': 0.0094,'з': 0.01641,
    'и': 0.07367,'й': 0.01208,'к': 0.03486,
    'л': 0.04343,'м': 0.03203,'н': 0.067,
    'о': 0.10983,'п': 0.02804,'р': 0.04746,
    'с': 0.05473,'т': 0.06318,'у': 0.02615,
    'ф': 0.00267,'х': 0.00966,'ц': 0.00486,
    'ч': 0.0145,'ш': 0.00718,'щ': 0.00361,
    'ъ': 0.00037,'ы': 0.01898,'ь': 0.01735,
    'ю': 0.00639,'я': 0.02001,
}

if request == 1:
    strings = []
    print("Введите несколько строк. Когда ввод необходимо будет закончить - нажмите Enter.")
    string = "Я строка"
    while string != "":
        string = input()
        strings.append(string)
    strings.remove("")
    print(strings)
    def solution(strings):
        counter = Counter(strings)
        chars = sum(counter.values())
        commonChar, commonCount = counter.most_common(1)[0]
        strFreq = commonCount/chars
        alphFreq = alphabet.get(commonChar,0)

        return abs(strFreq - alphFreq)
    print(sorted(strings, key=solution))

if request == 2:
    strings = []
    print("Введите несколько строк. Когда ввод необходимо будет закончить - нажмите Enter.")
    string = "Я строка"
    while string != "":
        string = input()
        strings.append(string)
    strings.remove("")
    print(strings)
    def solution(strings):
        counter = Counter(strings)
        chars = sum(counter.values())
        commonChar, commonCount = counter.most_common(1)[0]
        strFreq = commonCount/chars
        alphFreq = alphabet.get(commonChar,0)

        return abs(strFreq - alphFreq)**2
    print(sorted(strings, key=solution))
#В порядке увеличения разницы между количеством сочетаний «гласная-согласная» и «согласная-гласная» в строке.
#'аоуыиэеёюя'
#'бвгджзклмнпрстфхцчшщ'
if request == 3:
    strings = []
    print("Введите несколько строк. Когда ввод необходимо будет закончить - нажмите Enter.")
    string = "Я строка"
    while string != "":
        string = input()
        strings.append(string)
    strings.remove("")
    print(strings)
    def combinations(string):
        comboVC = 0
        comboCV = 0
        for i in range(len(string)-1):
            if string[i] in 'аоуыиэеёюя' and string[i+1] in 'бвгджзклмнпрстфхцчшщ':
                comboVC += 1
            if string[i] in 'бвгджзклмнпрстфхцчшщ'and string[i+1] in 'аоуыиэеёюя':
                comboCV += 1
        return comboVC, comboCV
    def solution(string):
        comboCV, comboVC = combinations(string)
        return abs(comboVC - comboCV)

    print(sorted(strings, key=solution))

if request == 4:
    strings = []
    print("Введите несколько строк. Когда ввод необходимо будет закончить - нажмите Enter.")
    string = "Я строка"
    while string != "":
        string = input()
        strings.append(string)
    strings.remove("")
    print(strings)
    def freqChar(strings):
        allStrings = ''.join(strings)
        frequency = Counter(allStrings)
        
        commonChar, commonCount = frequency.most_common(1)[0]
        return commonChar, commonCount

    def solution(string, common_count):
        frequency = string.count(common_character)
        return (frequency - common_count) ** 2
        
    common_character, common_count = freqChar(strings)

    print(sorted(strings, key=lambda s: solution(s, common_count)))   