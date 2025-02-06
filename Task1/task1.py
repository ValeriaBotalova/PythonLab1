def solution(number):
    divisors = []
    for i in range(2, int(number**0.5) + 1):
        while number%i == 0:
            divisors.append(i)
            number //= i
        else:
            i += 1
    if number>1:
        divisors.append(number)
    return(set(divisors))
print(max(solution(int(input("Введите число: ")))))