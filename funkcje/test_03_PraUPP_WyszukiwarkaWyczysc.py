def test_03_PraUPP_WyszukiwarkaWyczysc():
    """
    |
    | **Przypadek testowy: 3**

    | **Tytuł:** Pracownicy - Uprawnienia Pracownikow - Przywileje - Wyszukiwarka - Wyczyść

    | **Warunki początkowe:** Operator ma aktywne usługi: SA-EMPLOYEE-PRIVILEGES-LIST:ACCESS

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