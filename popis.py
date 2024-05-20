# Funkce, která kontroluje, zda je číslo v zadaném rozsahu a je sudé
def je_sude_a_v_rozsahu(cislo, minimum, maximum):
    # Vrátí True, pokud je číslo sudé a je v zadaném rozsahu, jinak False
    return (cislo % 2 == 0) and (minimum <= cislo <= maximum)

# Hlavní program
def main():
    # Vstup od uživatele (přetypovaný na integer)
    pocet_cisel = int(input("Zadejte počet čísel: "))
    
    #prázdné  pole
    cisla = []
    
    # Cyklus s pevným počtem opakování
    for i in range(pocet_cisel):
        # Vstup čísla od uživatele a přetypování na integer
        cislo = int(input(f"Zadejte číslo {i + 1}: "))
        # Přidání čísla do pole
        cisla.append(cislo)
    
    # Vstup minimální a maximální hodnoty rozsahu od uživatele (přetypovaný na integer)
    minimum = int(input("Zadejte minimální hodnotu rozsahu: "))
    maximum = int(input("Zadejte maximální hodnotu rozsahu: "))
    
    # Inicializace prázdného pole pro sudá čísla v rozsahu
    suda_cisla_v_rozsahu = []
    
    # Cyklus s podmínkou
    i = 0
    # Pokračuj, dokud index i je menší než délka pole cisla
    while i < len(cisla):
        # Přečti číslo z pole na pozici i
        cislo = cisla[i]
        # Pokud číslo je sudé a v rozsahu, přidej ho do pole sudých čísel rozsahu
        if je_sude_a_v_rozsahu(cislo, minimum, maximum):
            suda_cisla_v_rozsahu.append(cislo)
        # Zvýšení indexu i o 1
        i += 1
    
    # Výstup s přetypováním na řetězec
    if suda_cisla_v_rozsahu:
        # Pokud sudých čísel v rozsahu není prázdné, vypíšu sudá čísla
        print("Suda čísla v rozsahu jsou:", ', '.join(map(str, suda_cisla_v_rozsahu)))
    else:
        # Pokud pole sudých čísel v rozsahu je prázdné, vypíšu zprávu
        print("V poli nejsou žádná sudá čísla v zadaném rozsahu.")
    
    # Odebrání posledního čísla z pole, pokud pole není prázdné
    if suda_cisla_v_rozsahu:
        # Odeber poslední číslo z pole a ulož ho do proměnné
        posledni_sude = suda_cisla_v_rozsahu.pop()
        # Vytiskni odebrané číslo
        print("Poslední sudé číslo bylo odebráno:", posledni_sude)
    else:
        # Pokud pole sudých čísel v rozsahu je prázdné, vytiskni zprávu
        print("Není co odebrat, pole sudých čísel v rozsahu je prázdné.")

# Spuštění hlavního programu
if __name__ == "__main__":
    main()

