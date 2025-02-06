import random

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

sentence = input("Введите предложение:")
print(solution(sentence))
print(solution(sentence))
print(solution(sentence))
print(solution(sentence))
print(solution(sentence))
            