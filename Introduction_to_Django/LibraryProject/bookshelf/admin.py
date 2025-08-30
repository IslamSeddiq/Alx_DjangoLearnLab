from django.contrib import admin
from .models import Book
# Register your models here.

# Customize how Book is displayed in the admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in list view
    search_fields = ('title',)  # Add search box for these fields
    list_filter = ('publication_year',)  # Add filter sidebar for years

# Register Book with the custom admin
admin.site.register(Book, BookAdmin)
