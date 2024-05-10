import pandas as pd
import importlib
import re

# Wczytanie pliku CSV
df = pd.read_csv('check_description/SA_Pracownicy.csv')

# === Funkcje szukające ===
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

# === Funkcje wyciągające dane z CSV ===
def number_CSV(row):
    # Zwrócenie wartości komórki Nr
    return df.iloc[row, 1]

def title_CSV(row):
    # Zwrócenie wartości komórki Komponent
    return df.iloc[row, 3]

def prerequisites_CSV(row):
    # Zwrócenie wartości komórki Warunki wstępne oraz usunięcie \n
    return ' '.join(df.iloc[row, 6].split())

def steps_CSV(row):
    # Zwrócenie wartości komórki Kroki przypadku testowego
    return df.iloc[row, 5]

def results_CSV(row):
    # Zwrócenie wartości komórki Oczekiwany rezultat przypadku testowego
    return df.iloc[row, 7]

# === Funkcje wyciągające dane z opisu testów ===
def number_description(function):
    """Zwraca z opisu numer przypadku testowego"""
    make_list = function.__doc__.split()
    start = make_list.index('testowy:')
    make_list = make_list[start + 1:]
    end = make_list.index('|')
    make_list = make_list[:end]
    return ' '.join(make_list)[:-2]

def title_description(function):
    """Zwraca z opisu Tytuł"""
    make_list = function.__doc__.split()
    start = make_list.index('**Tytuł:**')
    make_list = make_list[start + 1:]
    end = make_list.index('|')
    make_list = make_list[:end]
    return ' '.join(make_list)

def prerequisites_description(function):
    """Zwraca z opisu warunki wstępne"""
    # Wyodrębnienie odpowiedniej zawartości
    make_list = function.__doc__.split()
    start = make_list.index('początkowe:**')
    make_list = make_list[start + 1:]
    end = make_list.index('**Kroki:**')
    make_list = ' '.join(make_list[:end - 1])
    # Formatowanie. Usunięcie numeracji jeśli istnieje
    if make_list[0] == "|":
        make_list = make_list.replace("|", "")
        make_list = re.sub(r"\s*\d+\.", "", make_list)[1:]
    return  make_list

def steps_description(function):
    """Zwraca z opisu kroki"""
    make_list = function.__doc__.split()
    start = make_list.index('**Kroki:**')
    make_list = make_list[start + 1:]
    end = make_list.index('**Oczekiwany')
    make_list = make_list[:end - 1]
    return ' '.join(make_list)

def results_description(function):
    """Zwraca z opisu oczekiwany rezultat"""
    make_list = function.__doc__.split()
    start = make_list.index('rezultat:**')
    make_list = make_list[start + 1:]
    end = make_list.index('|')
    make_list = make_list[:end]
    return ' '.join(make_list)

def final_check():
    list_of_tests = find_test_name(df)

    for index in range(0, len(list_of_tests)):
        mod = importlib.import_module(f"funkcje.{list_of_tests[index]}")
        my_fun = getattr(mod, f'{list_of_tests[index]}')
        error = False
        # Sprawdzenie Przypadku testowego
        number_in_csv = number_CSV(find_test_row(list_of_tests[index]))
        number_in_description = number_description(my_fun)
        if number_in_csv != number_in_description:
            print(f'{list_of_tests[index]} - Występują różnice w numeracji')
            error = True

        # Sprawdzenie Tytułu
        title_in_csv = title_CSV(find_test_row(list_of_tests[index]))
        title_in_description = title_description(my_fun)
        if title_in_csv != title_in_description:
            print(f'{list_of_tests[index]} - Występują różnice w tytule')
            error = True

        # Sprawdzenie Warunków początkowych
        prerequisites_in_csv = prerequisites_CSV(find_test_row(list_of_tests[index]))
        prerequisites_in_description = prerequisites_description(my_fun)
        if prerequisites_in_csv != prerequisites_in_description:
            print(f'{list_of_tests[index]} - Występują różnice w warunkach początkowych')
            error = True

        # Sprawdzenie Kroków

        # Sprawdzenie Oczekiwanego Rezultatu

        if not error:
            print(f'{list_of_tests[index]} - OK')

final_check()

# mod = importlib.import_module(f"funkcje.{find_test_name(df)[1]}")
# my_fun = getattr(mod, f'{find_test_name(df)[1]}')
# prerequisites_in_csv = prerequisites_CSV(find_test_row(find_test_name(df)[1]))
# prerequisites_in_description = prerequisites_description(my_fun)
# print()
# print(prerequisites_in_csv)
# print()
# print(prerequisites_in_description)
# print()
