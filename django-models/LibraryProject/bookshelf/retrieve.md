from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books  # Expected Output: <QuerySet [<Book: 1984>]>

# Retrieve a single book by title
book = Book.objects.get(title="1984")
book  # Expected Output: <Book: 1984>
