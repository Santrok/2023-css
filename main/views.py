from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main.forms import AddCarForm, RegistrationForm, LoginForm
from main.models import Car, Brand


# Create your views here.


def get_page(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    context = {
        "cars": cars,
        "brands": brands
    }

    return render(request, 'main.html', context)

def get_brand(request):
    brand_cars = Car.objects.filter(brand_id=request.GET.get('brand'))
    context = {
        'cars': brand_cars,
    }
    return render(request, 'brand.html', context)


def page_add_car(request):
    form = AddCarForm()
    if request.method == "POST":
        form = AddCarForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, 'add_car.html', context)


def detail_info(request, id):
    car = Car.objects.get(id=id)
    context = {
        'car': car
    }
    return render(request, 'detail.html', context)


def search(request):
    context = {

    }
    return render(request, 'search_result.html', context)


def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


def login_user(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Пользователь с такими данными не найден'
                context = {
                    'form': form,
                    'error_message': error_message
                }
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')

def kabinet(request):
    return render(request, 'kabinet.html')