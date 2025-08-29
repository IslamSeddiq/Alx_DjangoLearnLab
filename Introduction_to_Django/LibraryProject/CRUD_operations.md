# "Create Operation" 

from bookshelf.models import Book

# Create a new book instance
book1 = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Output
# <Book: 1984>

# "Retrieve Operation" 

from bookshelf.models import Book

# Get all books
books = Book.objects.all()
print(books)

# Get a single book by ID
book = Book.objects.get(id=1)
print(book)

# Output
# QuerySet [<Book: 1984>]>
# ('1984', 'George Orwell', 1949)

# "Update Operatio" 

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Output
# <Book: Nineteen Eighty-Four>
# QuerySet [<Book:Nineteen Eighty-Four>]>

# Delete the book
book = Book.objects.get(id=1)
book.delete()

Output

(1, {'bookshelf.Book': 1})