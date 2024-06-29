from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

def logout_controller(request):
    if request.user.is_authenticated:
        h = logout(request)
        return redirect('/board')
    else:
        return render(request, 'login_error.html')

def login_controller(request):
    if request.method == 'GET':
        return render(request, 'login_error.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authenticated = authenticate(request, username=username, password=password)
        if(authenticated is not None):
            login(request, authenticated)
            return redirect('/board')
        else:
            return render(request, 'login_error.html')


def sign_up(request):
    if request.method == 'GET':
        return render(request, template_name="sign_up.html")
    if request.method == 'POST':
        return render(request, template_name="sign_up.html")
