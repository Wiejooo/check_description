def test_02_PraUPP_Wyszukiwarka():


    """
    |
    | **Przypadek testowy: 2**

    | **Tytuł:** Pracownicy - Uprawnienia Pracowników - Przywileje - Wyszukiwark a

    | **Warunki początkowe:**

    | 1. W systemie są przywileje
    | 2. Operator ma aktywne usługi: SA-EMPLOYEE-PRIVILEGES-LIST:ACCESS

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