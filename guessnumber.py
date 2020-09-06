import random

def run():
    random_number = random.randint(1, 100)
    user_number = int(input('Choose a number from 1 to 100: '))
    while random_number != user_number:
        if user_number < random_number:
            print('Look for a bigger number')
        else:
            print('Look for a smaller number')
        user_number = int(input('Choose a number from 1 to 100: '))
    print('You Win!')


if __name__ == "__main__":
    run()