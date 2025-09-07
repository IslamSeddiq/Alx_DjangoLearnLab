import django
import os

# Setup Django (so script can run standalone)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


if __name__ == "__main__":
    # Example usage
    print("Books by George Orwell:")
    for book in books_by_author("George Orwell"):
        print(f"- {book.title}")

    print("\nBooks in Central Library:")
    for book in books_in_library("Central Library"):
        print(f"- {book.title}")

    print("\nLibrarian of Central Library:")
    print(librarian_for_library("Central Library").name)

