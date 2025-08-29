"Retrieve Operation" 

from bookshelf.models import Book

# Get all books
books = Book.objects.all()
print(books)

# Get a single book by ID
book = Book.objects.get(id=1)
print(book)