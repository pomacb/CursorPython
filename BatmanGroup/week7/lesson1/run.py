from lesson1.books import BookShell, Book


if __name__ == "__main__":
    shell_1 = BookShell()

    print(shell_1.consist())

    book_1 = Book("Memoirs of a Geisha", "Arthur Golden")
    book_2 = Book("A Game of Thrones", "George R.R. Martin")
    book_3 = Book("Great Expectations", "Charles Dickens")

    shell_1 += book_1
    # shell_1 += book_2
    # shell_1 += book_3

    print(book_1.author)
    print(shell_1.consist())
