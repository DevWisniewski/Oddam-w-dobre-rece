from django.shortcuts import render
from .models import Donation, Institution
from django.db.models import Sum  # Import funkcji agregującej


def index(request):
    total_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    supported_organizations = Institution.objects.count()

    context = {
        'total_bags': total_bags,
        'supported_organizations': supported_organizations,
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

