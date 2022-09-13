from django.contrib import admin
from .models import *
# Register your models here.

class LibraryAdmin(admin.ModelAdmin):
    list_display=['uuid','book_name','book_catagory','author_name','publication_name','created_at']

admin.site.register(Library,LibraryAdmin)
   

class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','email','password','created_at']

admin.site.register(User,UserAdmin)