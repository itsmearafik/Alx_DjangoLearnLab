from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    search_fields = ('title', 'author')

admin.site.register(Book) 

