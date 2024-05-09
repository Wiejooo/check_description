import pandas as pd
import importlib

# Wczytanie pliku CSV
df = pd.read_csv('check_description/SA_Pracownicy.csv')

def find_test_name(CSV):
    """Zwraca listę testów"""

    # Przygotowanie zmiennych
    list_of_tests = []
    index = 0
    column_tests_name = CSV.iloc[0:, 9]

    # Znalezienie testów i dodanie do listy
    while isinstance(column_tests_name[index], str):
        list_of_tests.append(column_tests_name[index])
        index += 1
    list_of_tests.remove('Nazwa pliku testowego')
    return list_of_tests

def find_test_row(name):
    # Znalezienie wiersza testu
    row_index = df[df.iloc[0:, 9]==name].index.values
    return int(row_index)

def komponent_CSV(row):
    # Zwrócenie wartości komórki Komponent
    return df.iloc[row, 3]

def komponent_description(function):
    make_list = function.__doc__.split()
    start = make_list.index('**Tytuł:**')
    make_list = make_list[start + 1:]
    end = make_list.index('|')
    make_list = make_list[:end]
    return ' '.join(make_list)


def final_check():
    list_of_tests = find_test_name(df)

    for index in range(0, len(list_of_tests)):
        mod = importlib.import_module(f"funkcje.{list_of_tests[index]}")
        my_fun = getattr(mod, f'{list_of_tests[index]}')
        # Sprawdzenie tytułu
        title_in_csv = komponent_CSV(find_test_row(list_of_tests[index]))
        title_in_description = komponent_description(my_fun)
        if title_in_csv != title_in_description:
            print(f'{list_of_tests[index]} - Występują różnice w tytule')
        else:
            print(f'{list_of_tests[index]} - OK')

        # Sprawdzenie Warunków początkowych

        # Sprawdzenie kroków

        # Sprawdzenie oczekiwanego rezultatu

final_check()
