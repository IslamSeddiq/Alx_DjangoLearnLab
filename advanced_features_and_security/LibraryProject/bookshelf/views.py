from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required

def search_books(request):
    query = request.GET.get("q")
    books = Book.objects.raw(f"SELECT * FROM bookshelf_book WHERE title LIKE '%{query}%'")
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # example placeholder
    return HttpResponse("Book created (only users with can_create can access this).")


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Editing book: {book.title} (only users with can_edit can access).")


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Deleting book: {book.title} (only users with can_delete can access).")

def home(request):
    return HttpResponse("Hello! This is the bookshelf home page.")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
# Create your views here.

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



