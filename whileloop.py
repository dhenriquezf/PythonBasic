def run():
    LIMIT = 100000

    accountant = 0
    power_two = 2 ** accountant
    while power_two < LIMIT:
        print('2 to the power of ' + str(accountant) + ' equals: ' + str(power_two))
        accountant += 1
        power_two = 2 ** accountant


if __name__ == "__main__":
    run()

