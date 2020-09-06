def run():
    # my_dictionary = {
    #     'key1': 1,
    #     'key2': 2,
    #     'key3': 3,
    # }
    # print(my_dictionary['key1'])
    # print(my_dictionary['key2'])
    # print(my_dictionary['key3'])

    country_population = {
        'Chile': 100000,
        'Argentina': 200000,
        'Colombia': 400000,
        'Japan': 550000,
    }

    # for country in country_population:
    #     print(country + ' tiene: ' + str(country_population[country]) + ' population')

    #loop of values
    # for country in country_population.values():
    #     print(country)

    #loop of items
    for country, population in country_population.items():
        print(country + ' has: ' + str(population) + ' population')


if __name__ == "__main__":
    run()