import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

ENGLISH = "English"
KOREAN = "Korean"
INDONESIAN = "Bahasa"
SPANISH= "Spanish"
OTHER = "Other"

class CustomUser(AbstractUser):
    # Add custom fields if needed
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Super User"
        verbose_name_plural = "Super Users"

# Create your models here.
class Staff(CustomUser):
    # Add custom fields if needed
    position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"

    def __str__(self):
        return self.first_name + " " + self.last_name  # You can return any meaningful representation

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', related_name='addresses', on_delete=models.CASCADE)  # Many addresses can belong to one customer
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country} - {self.postal_code}"

class Customer(CustomUser):
    cash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    favorite_genres = models.ManyToManyField('Genre', related_name="preferred_customers", blank=True)
    preferred_language = models.CharField(
        max_length=20, 
        choices=[
            (ENGLISH, "English"),
            (KOREAN, "Korean"),
            (INDONESIAN, "Bahasa"),
            (SPANISH, "Spanish"),
            (OTHER,"Other"),
        ], 
        default='English'
    )


    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def get_purchase_history(self):
        return Transaction.objects.filter(customer=self)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Book(models.Model):
    
    LANGUAGE_CHOICES =[
        (ENGLISH, "English"),
        (KOREAN, "Korean"),
        (INDONESIAN, "Bahasa"),
        (SPANISH, "Spanish"),
        (OTHER,"Other"),
    ]

    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=True, default = "Unknown author")
    publisher =  models.CharField(max_length=100, blank=True, default = "Unknown")
    pages = models.IntegerField(default = 0)
    book_id = models.UUIDField(
        primary_key=True,  # Makes it the primary key for the model
        default=uuid.uuid4,  # Automatically generate a new UUID
        editable=False  # Prevents manual editing in forms
    )
    pub_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='cover/', blank=True, null=True, default='default_cover.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    stock = models.IntegerField(default = 0)
    genres = models.ManyToManyField('Genre', blank=True)
    synopsis = models.TextField(blank=True, default="No Synopsis")

    language = models.CharField(
        max_length=20, 
        choices=LANGUAGE_CHOICES,
        default=OTHER
    )
    
    def is_in_stock(self):
        #Check if book stock isnt zero
        return self.stock > 0

    def get_customers(self):
        #Get any customer that ever buy this book
        return [transaction.customer for transaction in self.transactions.all()]

    def total_sales_quantity(self):
        #Get total quantity of this book that have been sold
        return sum(transaction.book_quantity for transaction in self.transactions.all())

    def total_sales_cash(self):
        #Get total of cash that this book has earned
        return sum(transaction.total_cash for transaction in self.transactions.all())

    def __str__(self):
        return self.title + " by " + self.author

class Genre(models.Model):
    FANTASY = "Fantasy"
    ADVENTURE = "Adventure"
    SCI_FI = "Sci-Fi"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    THRILLER = "Thriller"
    HISTORICAL_FICTION ="Historical Fiction"
    HORROR = "Horror"
    LITERARY = "Literary"
    YOUNG_ADULT = "Young Adult"
    NON_FICTION = "Non-Fiction"
    BIOGRAPHY = "Biography"
    HISTORY = "History"
    SCIENCE = "Science"
    TRAVEL = "Travel"
    COOKBOOK = "Cookbook"
    PHILOSOPHY = "Philosophy"
    ART = "Art"
    GRAPHIC_NOVEL = "Graphic Novel"
    POETRY = "Poetry"
    ANTHOLOGY = "Anthology"
    FICTION = "Fiction"

    # Genre choices
    GENRE_CHOICES = [
        (FANTASY, "Fantasy"),
        (ADVENTURE, "Adventure"),
        (SCI_FI, "Sci-Fi"),
        (MYSTERY, "Mystery"),
        (ROMANCE, "Romance"),
        (THRILLER, "Thriller"),
        (HISTORICAL_FICTION, "Historical Fiction"),
        (HORROR, "Horror"),
        (LITERARY, "Literary"),
        (YOUNG_ADULT, "Young Adult"),
        (NON_FICTION, "Non-Fiction"),
        (BIOGRAPHY, "Biography"),
        (HISTORY, "History"),
        (SCIENCE, "Science"),
        (TRAVEL, "Travel"),
        (COOKBOOK, "Cookbook"),
        (PHILOSOPHY, "Philosophy"),
        (ART, "Art"),
        (GRAPHIC_NOVEL, "Graphic Novel"),
        (POETRY, "Poetry"),
        (ANTHOLOGY, "Anthology"),
        (FICTION, "Fiction")

    ]

    # Fields for Genre model
    name = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    customer = models.ForeignKey(
        'Customer', 
        on_delete=models.CASCADE, 
        related_name='transactions'
    )
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='transactions')
    book_quantity = models.PositiveIntegerField(default=1)
    total_cash = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(default=now)
    

    def __str__(self):
        return f"Transaction {self.transaction_id}: {self.customer} bought {self.book.title} x{self.book_quantity} on {self.transaction_date}"