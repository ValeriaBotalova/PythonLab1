from termcolor import colored, cprint

def compositeOddDivisors(number):
    divisors = []
    for i in range(2, number + 1):
        if number % i == 0:
            compositeNumber = False
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    compositeNumber = True
                    break
            if compositeNumber and i % 2 != 0:
                divisors.append(i)
    return divisors

def productOfDigits(number):
    product = 1
    while number > 0:
        product *= (number%10)
        number //=10
    return product

def allDivisors(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(number//i)
    return set(divisors)

n = int(input("Введите число: "))
print("Это произведение всех цифр: " + str(productOfDigits(n)))
print("А это все делители произведения: " + colored(str(allDivisors(productOfDigits(n))), "light_magenta"))
print("Это все нечетные и непростые делители введеного числа: " + colored(str(compositeOddDivisors(n)), "light_magenta"))
nod = max(list(set(allDivisors(productOfDigits(n))) & set(compositeOddDivisors(n))))
print(colored("А это их НОД: " + str(nod), "yellow", attrs=['underline']))
