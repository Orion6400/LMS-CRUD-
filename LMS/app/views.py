from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import LibraryBookData,Signin,Login

class SignIn(View):
    def get(self,request):
        form = Signin()
        return render(request, 'core/sign_in.html',{'Form':form})
    def post(self,request):
        formdata = Signin(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('login')
        else:
            return render(request,'core/sign_in.html',{'Form':formdata})

class LogIn(View):
    def get(self,request):
        form = Login()
        return render(request, 'core/login.html',{'Form':form})
    def post(self,request):
        formdata = request.POST
        email = formdata.get('email')
        password = formdata.get('password')
        user_object = User.objects.filter(email=email,password=password)
        if user_object:
            request.session['current_admin'] = user_object[0].first_name+' '+user_object[0].last_name
            return redirect('home')
        else:
            return redirect('login')
          

class Home(View):
    def get(self,request):
        context = Library.objects.all()
        print(request.session['current_admin'])
        return render(request,'core/home.html',{'data':context,'admin':request.session['current_admin']})

class AddData(View):
    def get(self,request):
       form = LibraryBookData()
       return render(request,'core/adddata.html',{'Form':form,'admin':request.session['current_admin']})
    
    def post(self,request):
        formdata = LibraryBookData(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('add-data')
        else:
            return render(request,'app/adddata.html',{'Form':formdata,'admin':request.session['current_admin']})

class DeleteData(View):
    def post(self,request):
        post_value = request.POST
        uid = post_value.get('id')
        data = Library.objects.get(uuid=uid)
        data.delete()
        return redirect('/')

class EditData(View):
    def get(self,request,uuid):
        data = Library.objects.get(uuid=uuid)
        form = LibraryBookData(instance=data)
        return render(request,'core/edit-student.html',{'Form':form})
    def post(self,request,uuid):
        old_data = Library.objects.get(uuid=uuid)
        formdata = LibraryBookData(request.POST, instance=old_data)
        if formdata.is_valid():
            formdata.save()
            return redirect('/')
        

