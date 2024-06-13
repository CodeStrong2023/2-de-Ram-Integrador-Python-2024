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
