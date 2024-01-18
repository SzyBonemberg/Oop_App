class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def __str__(self):
        return (f"\nTitle: {self.title}\n"
                f"Author: {self.author}\n"
                f"Publication Year: {self.publication_year}\n"
                f"You can borrow this book: {self.is_available}")


class Library:
    def __init__(self):
        self.books = []  # Here we have all books in library
        self.borrow_books = []  # Here we have only books which have attribute is_available = False

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)

    def list_available_books(self):
        if len(self.books) < 0:
            return f"List is empty"
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title: str) -> str:
        if len(self.books) < 0:
            return f"You can't borrow book because in library we don't have any books"
        else:
            for book in self.books:
                if book.title == title:
                    self.borrow_books.append(book)
                    book.is_available = False
                    return f"Book now isn't available"
        return f"This book doesn't exist"

    def return_book(self, title) -> str:
        for book in self.books:
            if book.title == title:
                self.borrow_books.remove(book)
                book.is_available = True
                return f"Book now is available"
        return f"This book doesn't exist"


class Get_Data:

    @staticmethod
    def get_title():
        title = input("Enter the Title of book: ")
        return title

    @staticmethod
    def get_author():
        author = input("Enter the Author of this book: ")
        return author

    @staticmethod
    def publication_year():
        while True:
            try:
                year = int(input("Enter the year of publication this book: "))
            except ValueError:
                continue
            else:
                return year


def main():
    library = Library()
    while True:
        value = input("\nYou wanna add enter a\n"
                      "If you wanna borrow book enter b\n"
                      "If you wanna see all books enter s\n"
                      "Else if you wanna quit enter q: ").lower()
        if value == 'a':
            title = Get_Data.get_title()
            author = Get_Data.get_author()
            year = Get_Data.publication_year()
            book = Book(title=title, author=author, publication_year=year)
            library.add_book(book)
        elif value == 's':
            library.list_available_books()
        elif value == 'b':
            title = Get_Data.get_title()
            library.borrow_book(title=title)
        elif value == 'q':
            break
        else:
            print('You enter invalid data')
    print('Thank you its all for today')


if __name__ == '__main__':
    main()