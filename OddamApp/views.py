from django.shortcuts import render
from .models import Donation, Institution
from django.db.models import Sum  # Import funkcji agregującej
from django.core.paginator import Paginator



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

