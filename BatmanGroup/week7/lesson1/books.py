class BookShell:

    booklist = []

    def __add__(self, book: object):
        self.booklist.append(book)

    def __str__(self):
        # for book in self.booklist:
        # return f"Title: {book.title}, Author: {book.author}"
        return {self.booklist}


class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
