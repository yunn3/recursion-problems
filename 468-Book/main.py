class Book:

    author = "Stephen Hawkings"

    def __init__(self, title: str, year: str) -> None:

        self.title = title
        self.year = year


def printBookArray(books: list) -> None:

    for book in books:
        print(book.title + " written by " + book.author + " in " + book.year)


books = []

books.append(Book("How Did It All Begin?", "2021"))
books.append(Book("The Theory of Everything", "2010"))
books.append(Book("God Created the Integers", "2006"))

printBookArray(books)
