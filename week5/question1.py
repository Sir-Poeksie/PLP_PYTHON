class Book:
    def __init__(self, title, author, pages):
        self._title = title                # Encapsulated attribute
        self._author = author
        self._pages = pages

    def read(self):
        print(f"Reading '{self._title}' by {self._author}.")

    def get_summary(self):
        return f"'{self._title}' is a book with {self._pages} pages."


class ComicBook(Book):  # Inheritance
    def __init__(self, title, author, pages, illustrator):
        super().__init__(title, author, pages)  # Call the parent constructor
        self._illustrator = illustrator

    def read(self):
        print(f"Enjoying the comic '{self._title}' with art by {self._illustrator}!")

    def get_summary(self):
        return f"'{self._title}' is a comic book illustrated by {self._illustrator}."


# Example usage
book1 = Book("1984", "George Orwell", 328)
comic1 = ComicBook("Spider-Man", "Stan Lee", 50, "Steve Ditko")

book1.read()
print(book1.get_summary())

comic1.read()
print(comic1.get_summary())
