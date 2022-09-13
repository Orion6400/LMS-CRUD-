from django.db import models
import uuid
from django.core.validators import MinLengthValidator

class Library(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    book_name = models.CharField(max_length=200)
    book_catagory = models.CharField(max_length=200,null=True,blank=True)
    author_name = models.CharField(max_length=200,null=True,blank=True)
    publication_name = models.CharField(max_length=200,null=True,blank=True)
    book_summary = models.TextField(null=True,blank=True)
    created_at = models.TimeField(auto_now_add=True)


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=15,blank=True,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    created_at = models.TimeField(auto_now_add=True)

    




