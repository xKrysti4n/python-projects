
def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    elif number ==2:
        is_prime =True
    else:
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
    print(is_prime)

n = int(input("Check this number: "))
prime_checker(number=n)