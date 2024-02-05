from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import Property, Company

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('company_home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def company_home(request):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)  # get the company of the logged-in user
        properties = Property.objects.filter(company=company)  # get properties of this company
        return render(request, 'company_home.html', {'properties': properties})
    else:
        return redirect('login')

def property_create_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_home')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})
    