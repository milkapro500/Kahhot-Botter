def main():
    print("=====================================")
    print("         KAHHOT BOTER by Milkapro500")
    print("=====================================\n")

    print("=========== BOTY ===========")
    kahoot_pin = input("1 - Podaj PIN gry: ")

    base_name = input("2 - Podaj nazwę dla botów (np. Kamil): ")
    try:
        num_bots = int(input("3 - Podaj ilość botów: "))
    except ValueError:
        print("Nieprawidłowa liczba. Ustawiam 1.")
        num_bots = 1
    bots = [f"{base_name}{i+1}" for i in range(num_bots)]

    print("\n========= ODPOWIEDZI =========")
    print("4 - Losowe odpowiedzi")
    print("5 - Poprawne odpowiedzi (wymaga ID quizu)")
    answer_mode = input("Wybierz tryb odpowiadania: ")

    quiz_id = None
    if answer_mode.strip() == "5":
        quiz_id = input("Podaj ID quizu: ")

    print("\n====== ZARZĄDZANIE BOTAMI ======")
    print("6 - Rozłącz wszystkie boty")
    print("7 - Włącz/wyłącz odpowiedzi dla wszystkich botów")

    print("\nUtworzone boty:")
    print("{:<10} {:<20} {:<25}".format("ID", "Nazwa Bota", "Tryb odpowiadania"))
    for i, bot in enumerate(bots, start=1):
        mode = "Poprawne" if quiz_id else "Losowe"
        print("{:<10} {:<20} {:<25}".format(i, bot, mode))

    # TODO: Implement actual bot logic and controls here

if __name__ == "__main__":
    main()
