def palindrome(word):
    word = word.replace(' ', '').lower()
    if word[::] == word[::-1]:
        return True
    else:
        return False


def run():
    word = input('Write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print('Is palindrome')
    else:
        print('Isn\'t palindrome')


if __name__ == '__main__':
    run()