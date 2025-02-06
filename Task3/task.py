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
print(solution(str(input("Введите предложение: "))))