def prime_number(number):
    # accountant = 0
    # for i in range(1, number + 1):
    #     if i == 1 or i == number:
    #         continue
    #     if number % i == 0:
    #         accountant += 1

    # if accountant == 0:
    #     return True
    # else:
    #     return False

    accountant = 0
    i = 0
    while i < number:
        i += 1
        if number % i == 0:
            accountant += 1
    return accountant


def run():
    number = int(input('Write a number: '))
    if prime_number(number) == 2:
        print('Is prime')
    else:
        print('Isn\'t prime')


if __name__ == "__main__":
    run()