class Book:
  """
  Represents a book with title, author, and availability information.
  """
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.__is_checked_out = False  # Private attribute for availability

  def check_out(self):
    """
    Marks the book as checked out (unavailable).
    """
    self.__is_checked_out = True

  def return_book(self):
    """
    Marks the book as returned (available).
    """
    self.__is_checked_out = False

  def is_checked_out(self):
    """
    Returns True if the book is checked out, False otherwise.
    """
    return self.__is_checked_out

  def __str__(self):
    """
    Provides a user-friendly string representation of the book.
    """
    return f"{self.title} by {self.author}"


class Library:
  """
  Represents a library with a collection of books and methods for managing them.
  """
  def __init__(self):
    self._books = []  # Private list to store Book instances

  def add_book(self, book):
    """
    Adds a book to the library collection if it's a Book instance.
    """
    if isinstance(book, Book):
      self._books.append(book)
    else:
      print("Invalid book object. Please add a Book instance.")

  def check_out_book(self, title):
    """
    Attempts to check out a book by title, marking it unavailable if successful.
    """
    for book in self._books:
      if book.title == title and not book.is_checked_out():
        book.check_out()
        print(f"Successfully checked out '{title}'.")
        return
    print(f"Sorry, '{title}' is not available or does not exist.")

  def return_book(self, title):
    """
    Attempts to return a book by title, marking it available if successful.
    """
    for book in self._books:
      if book.title == title and book.is_checked_out():
        book.return_book()
        print(f"Successfully returned '{title}'.")
        return
    print(f"Sorry, '{title}' is already available or does not exist.")

  def list_available_books(self):
    """
    Prints a list of all available books (not checked out) in the library.
    """
    print("Available books:")
    for book in self._books:
      if not book.is_checked_out():
        print(book)
