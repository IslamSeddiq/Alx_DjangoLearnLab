"Delete Operation" 

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirming the deletion
all_books = Book.objects.all()
print(all_books)