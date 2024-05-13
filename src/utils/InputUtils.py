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
