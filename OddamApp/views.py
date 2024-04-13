from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def form(request):
    return render(request, 'form.html')

def form_confirmation(request):
    return render(request, 'form-confirmation.html')


# to są widoki testowe
def form1(request):
    return render(request, 'form1.html')

def form_confirmation1(request):
    return render(request, 'form-confirmation1.html')

def index1(request):
    return render(request, 'index1.html')

def login1(request):
    return render(request, 'login1.html')

def register1(request):
    return render(request, 'register1.html')

def base(request):
    return render(request, 'base.html')

def base_static(request):
    return render(request, 'base_static.html')