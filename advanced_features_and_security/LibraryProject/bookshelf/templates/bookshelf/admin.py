from django.contrib import admin
from .models import Book, Company, Department, Employee, Product, ProductDetail, Student, Course
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

# Customize how Book is displayed in the admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "full_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password", "full_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in list view
    search_fields = ('title',)  # Add search box for these fields
    list_filter = ('publication_year',)  # Add filter sidebar for years

# Register Book with the custom admin
# Company Admin
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name", "location")


# Department Admin
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
    search_fields = ("name",)
    list_filter = ("company",)


# Employee Admin
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "department")
    search_fields = ("name", "position")
    list_filter = ("department",)


# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


# ProductDetail Admin
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "manufacturer", "warranty_period")
    search_fields = ("manufacturer",)


# Student Admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_horizontal = ("courses",)  # Better UI for ManyToMany


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "credits")
    search_fields = ("title",)


# Registering all models
admin.site.register(Book, BookAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CustomUser, CustomUserAdmin)