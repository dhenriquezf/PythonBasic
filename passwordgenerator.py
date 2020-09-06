import random


def generator_password():
    capital_letters = ['A','B','C','D','E','F','G']
    lowercase = ['A','B','C','D','E','F','G']
    symbols = ['!','#','%','$','?','/',')']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    characters = capital_letters + lowercase + symbols + numbers
    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = ''.join(password)
    return password


def run():
    password = generator_password()
    print('Your new password is: ' + password)


if __name__ == "__main__":
    run()