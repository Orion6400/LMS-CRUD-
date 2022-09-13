from django import forms
from .models import Library,User


class LibraryBookData(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('book_name','book_catagory','author_name','publication_name','book_summary')
        widgets = {
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'book_catagory':forms.TextInput(attrs={'class':'form-control'}),
            'author_name':forms.TextInput(attrs={'class':'form-control'}),
            'publication_name':forms.TextInput(attrs={'class':'form-control'}),
            'book_summary':forms.TextInput(attrs={'class':'form-control'})
        }

class Signin(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','phone','email','password')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

