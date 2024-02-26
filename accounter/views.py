from django.core.paginator import Paginator
from django.shortcuts import render
from .models import PropertyExpense, Income, Mile

def expenses(request):
    expense = PropertyExpense.objects.all()

    expense_paginator = Paginator(expense, 10)

    page_number = request.GET.get('page')
    expense_page_obj = expense_paginator.get_page(page_number)
    

    return render(request, 'expenses.html', {'expense_page_obj': expense_page_obj})