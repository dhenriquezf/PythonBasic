# def print_message():
#     print('Especial message: ')
#     print('Im learning to use functions!')

# print_message()
# print_message()
# print_message()

# def conversation(option):
#     print('Hi!')
#     print('How are you?')
#     print('You chose option ' + str(option))
#     print('Bye!')

# option = int(input('Choose an option (1,2,3): '))

# if option == 1:
#     conversation(option)
# elif option == 2:
#     conversation(option)
# elif option == 3:
#     conversation(option)
# else:
#     print('You chose the correct option')

def sum(a, b):
    print('Sum two numbers')
    return a + b

response = sum(4,5)
print('The result is: '+ str(response))