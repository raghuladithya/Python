class India:
    def capital(self):
        print("Delhi is the capital of India")

    def Language(self):
        print("Hindi is the Language of India")

    def type(self):
        print("India is developing country")

class USA:
    def capital(self):
        print("Washington is the capital of USA")

    def Language(self):
        print("English is the capital of USA ")

    def type(self):
        print("USA is developed country")

objind = India()
objusa = USA()

for country in (objind,objusa):
    country.capital()
    country.Language()
    country.type()
