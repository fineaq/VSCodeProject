from django.contrib import admin
from .models import *

# Inline for the Address model in the Customer admin page
class AddressInline(admin.StackedInline):
    model = Address  # Directly use the Address model
    extra = 1  # Number of empty forms displayed

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'position')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'cash')
    inlines = [AddressInline]  # Add AddressInline to Customer admin

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country', 'postal_code')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the admin list view
    search_fields = ('name',)  # Add a search bar for the name field