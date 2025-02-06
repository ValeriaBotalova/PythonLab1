import random

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

print("Получившийся флаг:", solution(futureFlag))