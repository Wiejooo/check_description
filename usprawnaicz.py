import pandas as pd


# import inspect
# import os

# def find_functions(funkcje_dir):
#     for filename in os.listdir(funkcje_dir):
#         if filename.endswith('.py'):
#             filepath = os.path.join(funkcje_dir, filename)
#             with open(filepath, 'r') as f:
#                 module_name = os.path.splitext(filename)[0]
#                 module = __import__(f'funkcje.{module_name}', fromlist=[module_name])
#                 for name, obj in inspect.getmembers(module):
#                     if inspect.isfunction(obj):
#                         yield name, obj

# funkcje = list(find_functions('sprawdzOpis/funkcje'))
# print(funkcje.__doc__)

exec("funkcje/test_01_PraUPP.py", globals())
funkcja = globals()['test_01_PraUPP']
print(funkcja())

def test_02_PraUPP_Wyszukiwarka():


    """
    |
    | **Przypadek testowy: 2**

    | **Tytuł:** Pracownicy - Uprawnienia Pracowników - Przywileje - Wyszukiwarka

    | **Warunki początkowe:**

    | 1. W systemie są przywileje.
    | 2. Operator systemu posiada uprawnienia: SA-EMPLOYEE-PRIVILEGES-LIST:ACCESS.

    | **Kroki:**

    | 1. Operator loguje się do serwisu SA
    | 2. Operator wchodzi w "Pracownicy"
    | 3. Operator rozwija listę "Uprawnienia Pracowników"
    | 4. Operator wchodzi w "Przywileje"
    | 5. Operator uzupełnia "Czynność"
    | 6. Operator uzupełnia "Modyfikator"
    | 7. Operator klika "Szukaj"

    | **Oczekiwany rezultat:** System wyświetla ekran "Przywileje" z wyszukiwarką przywilejów. System
                                wyświetla listę przywilejów spełniających kryteria wyszukiwania.

    | **Warunki końcowe:** Ekran "Przywileje" z szukanymi rekordami.

    """

def test_03_PraUPP_WyszukiwarkaWyczysc():
    """
    |
    | **Przypadek testowy: 3**

    | **Tytuł:** Pracownicy - Uprawnienia Pracownikow - Przywileje - Wyszukiwarka - Wyczyść

    | **Warunki początkowe:** Operator systemu posiada uprawnienia: SA-EMPLOYEE-PRIVILEGES-LIST:ACCESS.

    | **Kroki:**

    | 1. Operator loguje się do serwisu SA
    | 2. Operator wchodzi w "Pracownicy"
    | 3. Operator rozwija listę "Uprawnienia Pracowników"
    | 4. Operator wchodzi w "Przywileje"
    | 5. Operator uzupełnia "Czynność"
    | 6. Operator uzupełnia "Modyfikator"
    | 7. Operator klika "Wyczyść"

    | **Oczekiwany rezultat:** System wyświetla ekran "Przywileje" z wyszukiwarką przywilejów.
                                System czyści pola wyszukiwania wypełnione przez Operatora systemu.

    | **Warunki końcowe:** Kryteria wyszukiwania zostają wyczyszczone.

    """


# test_01_PraUPP()

df = pd.read_csv('IF-game/SA_Pracownicy.csv')

def find_test_name(CSV):
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
    for index in range(0, len(find_test_name(df))):
        # Sprawdzenie tytułu
        title_in_csv = komponent_CSV(find_test_row(find_test_name(df)[index]))
        title_in_description = komponent_description(eval(find_test_name(df)[index]))
        if title_in_csv != title_in_description:
            print(f'{find_test_name(df)[index]} - Występują różnice w tytule')
        else:
            print(f'{find_test_name(df)[index]} - OK')

        # Sprawdzenie Warunków początkowych

        # Sprawdzenie kroków

        # Sprawdzenie oczekiwanego rezultatu

# final_check()


# print(type(test_01_PraUPP))
# print(type(eval(find_test_name(df)[0])))