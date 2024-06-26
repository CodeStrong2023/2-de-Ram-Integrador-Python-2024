import re


class InputUtils:
    @staticmethod
    def str_input(input_string):
        entry = input(input_string)
        if len(input_string) < 1:
            print("Debe ingresar al menos un caracter")
            return InputUtils.str_input(input_string)
        else:
            return entry

    @staticmethod
    def int_input(input_string, max_len):
        entry = input(input_string)
        if entry.isnumeric() and len(entry) <= max_len:
            return int(entry)
        if len(entry) < 1:
            print("Debe ingresar al menos un caracter")
            return InputUtils.int_input(input_string, max_len)
        if len(entry) > max_len:
            print(f"No puede ingresar más de {max_len} número(s)")
            return InputUtils.int_input(input_string, max_len)

    @staticmethod
    def email_input(email):
        entry = input(email)
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, entry):
            return entry
        else:
            print("Debes ingresar un email válido")
            InputUtils.email_input(email)
