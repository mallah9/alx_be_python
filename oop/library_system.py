class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library collection.

        Args:
            book (Book, EBook, or PrintBook): The book instance to add.
        """
        self.books.append(book)

    def list_books(self):
        """Prints details of all books in the library."""
        for book in self.books:
            # Use isinstance to check book type and print specific details
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:  # Regular Book
                print(f"Book: {book.title} by {book.author}")
