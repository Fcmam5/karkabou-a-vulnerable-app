import logging
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import Band, Musician, Wilaya
from .forms import RegistrationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect


def band_list(request):
    query = request.GET.get('search', '')
    wilaya_filter = request.GET.get('wilaya', '')

    bands = Band.objects.all()

    if query:
        bands = bands.filter(name__icontains=query)

    if wilaya_filter:
        bands = bands.filter(wilaya=wilaya_filter)

    context = {
        'bands': bands,
        'wilayas': Wilaya.choices, 
    }
    return render(request, 'band_list.html', context)

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    musicians = Musician.objects.filter(band=band)

    context = {
        'band': band,
        'musicians': musicians,
    }
    
    return render(request, 'band_detail.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logging.info("Successfully registered user with email: %s ... Logging in" % user.email)
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def index_page(request):
    return render(request, 'index.html')

def privacy_policy_view(request):
    return render(request, 'tnc/privacy.html')

def terms_of_service_view(request):
    return render(request, 'tnc/terms_of_service.html')