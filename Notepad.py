

import glob, os

class Poznamky:

    def __init__(self):

        self.menu = ("1.    Zobrazit poznamky\n"
                     "2.    Nova poznamka\n"
                     "3.    Upravit poznamku\n"
                     "4.    Smazat poznamku\n"
                     "5.    Konec poznamek\n")



        self. zobrazit_poznamku = glob.glob("*.txt")
        self.zobrazit_poznamku.sort()



    def zobrazit_menu(self):

        self.zastaveni = True
        while self.zastaveni:
            print()
            print(self.menu)

            vstup = input()
            if vstup == "1":
                self.zobrazit_poznamky()

            elif vstup == "2":
                self.nova_poznamka()

            elif vstup == "3":
                self.uprava_poznamky()

            elif vstup == "4":
                self.odstraneni_poznamek()

            elif vstup == "5":
                self.konec_programu()


    def uprava_poznamky(self):

        for i in self.zobrazit_poznamku:
            print(i, end=",  ")

        print()
        nazev_souboru = input() + ".txt"
        print("Poznamkovy blok:")
        print()
        with open(nazev_souboru, "r") as textovy_soubor:
            print(textovy_soubor.read())

        enter = True
        with open(nazev_souboru, "a") as textovy_soubor:
            while enter:
                uzivatel = input()
                textovy_soubor.write(uzivatel + "\n")
                if uzivatel == "Quit":
                    self.zobrazit_poznamku.append(nazev_souboru)
                    break


    def konec_programu(self):

        self.zastaveni = False
        print("Vypnuti programu")



    def zobrazit_poznamky(self):


        for i in self.zobrazit_poznamku:

            print(i, end=",  ")

        print()
        if len(self.zobrazit_poznamku) == 0:

            print("Nemate zadne soubory.")
            print()



    def nova_poznamka(self):
        print("Napište název souboru")

        enter = True
        nazev_souboru = input() + ".txt"

        print("Poznamkovy blok:")
        print()
        with open(nazev_souboru, "w") as textovy_soubor:
            while enter:
                uzivatel = input()
                textovy_soubor.write(uzivatel + "\n")
                if uzivatel == "Quit":
                    self.zobrazit_poznamku.append(nazev_souboru)
                    break


    def odstraneni_poznamek(self):

        for i in self.zobrazit_poznamku:
            print(i, end=", ")
        print()
        print("Kterou si prejete smazat?")

        smazani = int(input())

        os.remove(self.zobrazit_poznamku[smazani])
        self.zobrazit_poznamku.remove(self.zobrazit_poznamku[smazani])

poznamky = Poznamky()

poznamky.zobrazit_menu()





