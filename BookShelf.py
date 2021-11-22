from Book import Book


class BookShelf:

    def __init__(self):
        self.books = []
        self.size = 0

    def get_books(self):
        return self.books

    def get_size(self):
        return self.size

    def add_book(self, book):
        self.books.append(book)
        self.size += 1

    # def add_book(self, title, author):
    #     self.books.append(Book(title, author))
    #     self.size += 1

    def remove_book(self, title, author):
        for book in self.books:
            if book.get_title().__eq__(title) & book.get_author().__eq__(author):
                self.books.remove(book)
                self.size -= 1

    def print_shelf(self):
        for book in self.books:
            book.print_book()
