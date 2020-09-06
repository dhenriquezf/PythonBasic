def converter(converter_type, dollar_value):
    pesos = input('How many '+ converter_type +' pesos do you have?: ')
    pesos = float(pesos)
    dollars = pesos / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print('You have $' + dollars + ' dollars')

menu = """
Welcome to converter of money to dollars $$
1 - Chilean pesos
2 - Colombian pesos
3 - Argentines pesos

Choose an option: """

option = int(input(menu))

if option == 1:
    converter('chilean', 771.50)
elif option == 2:
    converter('colombian', 3715.01)
elif option == 3:
    converter('argentines', 74.44)
else:
    print('Error, you don\'t select a valid option. Bye!')
