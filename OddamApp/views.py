from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Donation, Institution
from django.db.models import Sum  # Import funkcji agregującej
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

def index(request):
    total_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    supported_organizations = Institution.objects.count()

    # Pobieranie instytucji według typu z paginacją
    foundation_list = Institution.objects.filter(type=Institution.FUNDACJA).order_by('id')
    ngo_list = Institution.objects.filter(type=Institution.ORGANIZACJA_POZARZADOWA).order_by('id')
    local_collection_list = Institution.objects.filter(type=Institution.ZBIORKA_LOKALNA).order_by('id')

    paginator_foundation = Paginator(foundation_list, 2)
    paginator_ngo = Paginator(ngo_list, 2)
    paginator_local_collection = Paginator(local_collection_list, 2)

    page_number_foundation = request.GET.get('page_foundation')
    page_number_ngo = request.GET.get('page_ngo')
    page_number_local_collection = request.GET.get('page_local_collection')

    foundations = paginator_foundation.get_page(page_number_foundation)
    ngos = paginator_ngo.get_page(page_number_ngo)
    local_collections = paginator_local_collection.get_page(page_number_local_collection)

    context = {
        'total_bags': total_bags,
        'supported_organizations': supported_organizations,
        'foundations': foundations,
        'ngos': ngos,
        'local_collections': local_collections,
    }
    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Przekierowanie na stronę główną
        else:
            # Jeśli użytkownik nie istnieje, przekieruj do rejestracji
            return redirect('register')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})



def form(request):
    return render(request, 'form.html')


def form_confirmation(request):
    return render(request, 'form-confirmation.html')


def base(request):
    return render(request, 'base.html')


def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'settings.html')


def logout_view(request):
    logout(request)
    return redirect('/')  # Przekierowanie na stronę główną po wylogowaniu