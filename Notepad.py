"""Program used for creating, editing, deleting notes on the command line."""

import glob, os

class Notepad:

    def __init__(self):

        self.menu = ("1.    List of saved notes\n"
                     "2.    New note\n"
                     "3.    Edit note\n"
                     "4.    Delete note\n"
                     "5.    End of program\n")


        self. view_note = glob.glob("*.txt")
        self.view_note.sort()


    def view_menu(self):

        self.stopping_the_program = True
        while self.stopping_the_program:
            print()
            print(self.menu)

            input_from_keyboard = input()
            if input_from_keyboard == "1":
                self.list_of_saved_notes()

            elif input_from_keyboard == "2":
                self.text_file()

            elif input_from_keyboard == "3":
                self.edit_note()

            elif input_from_keyboard == "4":
                self.delete_note()

            elif input_from_keyboard == "5":
                self.end_of_program()


    def edit_note(self):

        for i in self.view_note:
            print(i, end=",  ")

        print("\nEnter a name for the note:")
        print()
        name_of_file = input() + ".txt"
        print("Notepad:")
        print()

        with open(name_of_file, "r") as text_file:
            print(text_file.read())

        cycle = True
        with open(name_of_file, "a") as text_file:
            while cycle:
                user = input()
                if user == "Quit":
                    break
                text_file.write(user + "\n")



    def end_of_program(self):

        self.stopping_the_program = False
        print("Notepad off")



    def list_of_saved_notes(self):


        for note in self.view_note:

            print(note, end=",  ")

        print()
        if len(self.view_note) == 0:

            print("You have no files.")
            print()



    def text_file(self):
        print("Enter the filename:")

        enter = True
        filename = input() + ".txt"

        print("Notepad: ")
        print()
        with open(filename, "w") as text_file:
            while enter:
                user = input()

                if user == "Quit":
                    break

                text_file.write(user + "\n")
            self.view_note.append(filename)


    def delete_note(self):

        for i in self.view_note:
            print(i, end=", ")
        print()
        print("Which do you want to delete?")

        delete = int(input())

        os.remove(self.view_note[delete])
        self.view_note.remove(self.view_note[delete])


note = Notepad()
note.view_menu()





