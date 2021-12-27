from django.shortcuts import render
from .models import UserLogin

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        Userlogin = UserLogin(email=email, password=password)
        Userlogin.save()
        print(UserLogin.objects.all().values())
    return render(request, 'index.html')
