class Prece:
    PVN = 0.21  # PVN likme 21%

    def __init__(self):
        self.nosaukums = input("Ievadi preces nosaukumu: ")
        self.cena = float(input("Ievadi preces cenu (€): "))

    def izvade(self):
        cena_ar_pvn = round(self.cena * (1 + Prece.PVN), 2)
        print("\n--- Preces dati ---")
        print(f"Nosaukums: {self.nosaukums}")
        print(f"Cena (bez PVN): {self.cena:.2f} €")
        print(f"Cena (ar PVN): {cena_ar_pvn:.2f} €")


# Ja palaid šo failu tieši
if __name__ == "__main__":
    prece = Prece()
    prece.izvade()
