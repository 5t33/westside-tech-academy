
class Book:
    def __init__(self, title):
        self.title = title
        print("hello world")

    def funk(self, num):
        print(self.title)
        print(num)


book1 = Book("To Kill a Mockingbird")
book2 = Book("Catch 22")

book1.funk(2)