import re


class InputUtils:
    @staticmethod
    def str_input(input_string):
        entry = input(input_string)
        return entry

    @staticmethod
    def int_input(input_string):
        entry = input(input_string)
        if entry.isnumeric():
            return int(entry)
        else:
            print("Debe ingresar un número")
            return InputUtils.int_input(input_string)

    @staticmethod
    def character_detector(str_input):
        while True:
            if len(str_input) < 1:
                print("Debe ingresar al menos un caracter")
            else:
                break

    @staticmethod
    def email_input(email):
        entry = input(email)
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, entry):
            return entry
        else:
            print("Debes ingresar un email válido")
            InputUtils.email_input(email)
