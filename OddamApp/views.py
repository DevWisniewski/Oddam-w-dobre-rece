from django.shortcuts import render
from .models import Donation, Institution
from django.db.models import Sum  # Import funkcji agregującej


def index(request):
    total_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    supported_organizations = Institution.objects.count()

    # Pobieranie instytucji według typu
    foundations = Institution.objects.filter(type=Institution.FUNDACJA)
    ngos = Institution.objects.filter(type=Institution.ORGANIZACJA_POZARZADOWA)
    local_collections = Institution.objects.filter(type=Institution.ZBIORKA_LOKALNA)

    context = {
        'total_bags': total_bags,
        'supported_organizations': supported_organizations,
        'foundations': foundations,
        'ngos': ngos,
        'local_collections': local_collections,
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def form(request):
    return render(request, 'form.html')


def form_confirmation(request):
    return render(request, 'form-confirmation.html')


def base(request):
    return render(request, 'base.html')

