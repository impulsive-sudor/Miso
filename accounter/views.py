from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Company

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
        return render(request, 'company_home.html')
    else:
        return redirect('login')

# show all data in the company model