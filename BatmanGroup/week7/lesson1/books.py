class BookShell:

    def __init__(self, shell_number: int):
        self.shell_number = shell_number
        self.booklist = []

    def __add__(self, book: object):
        self.booklist.append(book)
        return self

    def show(self):
        print(f"Book shell #{self.shell_number} has books:")
        for book in self.booklist:
            print(f"Title: {book.title}, Author: {book.author}")


class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
