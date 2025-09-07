from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    

class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employees")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.position}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="detail")
    description = models.TextField()
    manufacturer = models.CharField(max_length=200)
    warranty_period = models.IntegerField(help_text="Warranty in months")

    def __str__(self):
        return f"Details for {self.product.name}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    credits = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return self.name
