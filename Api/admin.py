from django.contrib import admin
from .models import *
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

admin.site.register(Books, BooksAdmin)

admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quizzes)