from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView
from django.views.generic import DetailView

# Create your views here.
# def hello_view(request):
#     return HttpResponse("Hello World!")

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, "books/book_list.html", {"books": books})


class HelloView(TemplateView):
    """A class-based view rendering a template named 'hello.html'."""
    template_name = "hello/hello.html"


class BookDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'  # This will be used in the template

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context
        book = self.get_object()  # Current book instance

        # If you have a method in your model for ratings, use it
        if hasattr(book, "get_average_rating"):
            context['average_rating'] = book.get_average_rating()
        else:
            context['average_rating'] = None  # fallback

        return context
