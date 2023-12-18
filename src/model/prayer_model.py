class Prayer:
    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def set_title(self, title):
        self.__title = title

    def set_text(self, text):
        self.__text = text

    def __repr__(self):
        return f"Prayer('{self.__title}', '{self.__text}')"
