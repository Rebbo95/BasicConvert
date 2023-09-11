def volume():
    print("Konvertera mellan volymenheter:")
    print("1. Från liter till andra enheter")
    print("2. Från andra enheter till liter")

    choice = int(input("Välj alternativ (1 eller 2): "))

    if choice == 1:
        # Konvertera från liter till andra enheter
        Liter = float(input("Ange antal liter: "))
        Milliliter = Liter * 1000
        Centiliter = Liter * 100
        Deciliter = Liter * 10
        Cubic_Dm = Liter * 1
        Cubic_Meter = Liter / 1000

        print("Milliliter:", Milliliter)
        print("Centiliter:", Centiliter)
        print("Deciliter:", Deciliter)
        print("Kubikdecimeter (liter):", Cubic_Dm)
        print("Kubikmeter:", Cubic_Meter)

    elif choice == 2:
        # Konvertera från andra enheter till liter
        print("Konvertera till liter:")
        print("1. Milliliter")
        print("2. Centiliter")
        print("3. Deciliter")
        print("4. Kubikdecimeter (liter)")
        print("5. Kubikmeter")

        unit_choice = int(input("Välj enhet (1 till 5): ")) #
        value = float(input("Ange mängden i vald enhet: "))

        if unit_choice == 1:
            Liter = value / 1000
        elif unit_choice == 2:
            Liter = value / 100
        elif unit_choice == 3:
            Liter = value / 10
        elif unit_choice == 4:
            Liter = value
        elif unit_choice == 5:
            Liter = value * 1000
        else:
            print("Ogiltigt val av enhet.")
            return

        print("Liter:", Liter)

    else:
        print("Ogiltigt val av alternativ.")

volume()