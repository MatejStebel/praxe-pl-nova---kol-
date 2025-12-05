úkoly = []
print("*******************************")
print("\nVítejte v plánovači úkolů!\n")
print("*******************************")

def přidat_úkol():
    název = input("\nZadejte název úkolu: ")
    předmět = input("\nZadejte předmět: ")
    datum_odevzdání = input("Zadejte datum odevzdání (DD-MM-RRRR): ")
    úkoly.append({"název": název, "předmět": předmět, "datum_odevzdání": datum_odevzdání})
    print("\nÚkol přidán.")

def zobrazit_úkoly():
    if not úkoly:
        print("\nŽádné úkoly nejsou zadány.")
        return
    for i, úkol in enumerate(úkoly):
        print(f"\nČíslo úkolu: {i}\n      Název: {úkol['název']}\n      Předmět: {úkol['předmět']}\n      Datum odevzdání: {úkol['datum_odevzdání']}")

def odstranit_úkol():
    zobrazit_úkoly()
    index = int(input("\nZadejte číslo úkolu k odstranění: "))
    if 0 <= index < len(úkoly):
        úkoly.pop(index)
        print("\nÚkol odstraněn.")
    else:
        print("\nNeplatné číslo úkolu.")

def konec():
    print("\nProgram ukončen.")
    exit()

def hlavní_menu():
    print("\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    print("\nVitejte v hlavním menu.\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    print("1. Přidat úkol")
    print("2. Zobrazit úkoly")
    print("3. Odstranit úkol")
    print("4. Konec")
    volba = input("\nZadejte číslo akce, kterou chcete provést: ")
    if volba == "1":
        přidat_úkol()
    elif volba == "2":
        zobrazit_úkoly()
    elif volba == "3":
        odstranit_úkol()
    elif volba == "4":
        konec()
    else:
        print("\nŠpatné číslo, zadejte jiné číslo.")
        hlavní_menu()
while True:
    hlavní_menu()