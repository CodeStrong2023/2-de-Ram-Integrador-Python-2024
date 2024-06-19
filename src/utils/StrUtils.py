class StrUtils:
    @staticmethod
    def create_header(str_header):
        print("")
        print(f"{'=' * 12} {str(str_header).upper()} {'=' * 12}")
        print("")

    @staticmethod
    def error_message(message):
        print("")
        print(f"{'-' * (len(message) + 11)} ")
        print(f"| Error: {message} |")
        print(f"{'-' * (len(message) + 11)} ")

    @staticmethod
    def display_app_header():
        paw_print = """
                 .-"-.
                /|6 6|\\
               {/(_0_)\\}
                _/ ^ \\_
               (/ /^\\ \\)-'
                ""' '""
            """
        app_name = "Bienvenidos a Adoptame"
        print(paw_print)
        print(app_name.center(40, " "))
        print("=" * 40)