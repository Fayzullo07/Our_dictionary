import os


class Our_dictionary:
    def __init__(self):
        self.eng_word = None
        self.uz_word = None

    def system_entrance(self):
        self.cls()
        options = ['1', '2', '3', '4']
        self.print_messege()
        input_choice = input(">>>: ").strip()
        while self.is_string_empty(input_choice) or input_choice not in options:
            self.cls()
            self.print_messege()
            input_choice = input(">>>: ").strip()

        if input_choice == options[0]:
            return self.add_new_word()
        elif input_choice == options[1]:
            return self.search_word()
        elif input_choice == options[2]:
            return self.show_words()
        else:
            return self.go_out()

    def add_new_word(self):
        self.cls()
        input_eng_word = input("English: ").strip()
        while self.is_string_empty(input_eng_word) or not input_eng_word.isalpha():
            self.cls()
            input_eng_word = input("English: ").strip()

        input_uz_word = input("Uzbek: ")
    def show_words(self):
        pass

    def search_word(self):
        pass

    def go_out(self):
        pass

    @staticmethod
    def print_messege():
        print("""
        Add new word [1]
        Search word  [2]
        Show word    [3]
        Go out       [4]
        """)

    @staticmethod
    def cls():
        os.system("clear")

    @staticmethod
    def is_string_empty(str_):
        return not bool(str_)


dict1 = Our_dictionary()
dict1.system_entrance()