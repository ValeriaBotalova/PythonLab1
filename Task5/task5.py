#Дана строка. Необходимо найти все даты, которые описаны в виде "31 февраля 2007".

import re

def solution(sentence):
    pattern = r'\b(\d{1,2})\s+([А-ЯЁа-яё]+)\s+(\d{4})\b'
    date = re.findall(pattern, sentence)
    datesList = ['{} {} {}'.format(day, month, year) for day, month, year in date]
    return datesList
sentence = "Сегодня 7 февраля 2025 года, хотя я бы хотела 8 ноября 25 года. Но на самом деле лучшая дата - 5 мая 2005 года. Или же 05.05.2005."
print(solution(sentence))