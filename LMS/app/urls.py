"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *
urlpatterns = [
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    path('', LogIn.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),
    path('add-data/',AddData.as_view(),name='add-data'),
    path('delete-data/',DeleteData.as_view(),name='delete-data'),
    path('edit-data/<uuid>/',EditData.as_view(),name='edit-data')

]
