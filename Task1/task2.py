def solution(number):
    digits = []
    product = 1
    while number > 0:
        if (number%10)%5 != 0: 
            digits.append(number%10)
            product *= (number%10)
            number //= 10
        else: number //= 10
    return digits, product
print(solution(int(input("Введите число: "))))