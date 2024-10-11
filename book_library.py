# Class definition for a Book with basic attributes
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

# Class definition for the Library, which holds a collection of books
class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list of books

    # Method to add a new book to the library
    def add_book(self, book):
        self.books.append(book)

    # Method to search for books by title
    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    # Method to remove a book by its title
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    # Method to print the details of all books in the library
    def show_books(self):
        if not self.books:
            print("The library is empty")
        else:
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}")

# Creating the library and adding some books to it
library = Library()
book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display the current books in the library
library.show_books()

# Allow the user to interact with the library by searching, adding, or removing books
while True:
    print("Options: 1) Add Book, 2) Search Book, 3) Remove Book, 4) Show Books, 5) Quit")
    choice = input("Enter your choice: ")

    # Add a new book to the library
    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        new_book = Book(title, author, year, genre)
        library.add_book(new_book)
        print("Book added successfully!")
    
    # Search for a book by its title
    elif choice == "2":
        search_title = input("Enter the title to search: ")
        found_book = library.search_by_title(search_title)
        if found_book:
            print(f"Book Found - Title: {found_book.title}, Author: {found_book.author}, Year: {found_book.year}, Genre: {found_book.genre}")
        else:
            print("Book not found")
    
    # Remove a book by its title
    elif choice == "3":
        remove_title = input("Enter the title of the book to remove: ")
        removed = library.remove_book(remove_title)
        if removed:
            print("Book removed successfully!")
        else:
            print("Book not found")
    
    # Show all books in the library
    elif choice == "4":
        library.show_books()
    
    # Quit the program
    elif choice == "5":
        print("Exiting the program...")
        break

    else:
        print("Invalid option. Please try again.")
