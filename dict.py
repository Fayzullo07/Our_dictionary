import os
class Our_dictionary:
    def __init__(self):
        self.eng_word = None
        self.uz_word = None

    def system_intranse(self):
        pass

    def add_new_word(self):
        pass

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

dict1 = Our_dictionary()
