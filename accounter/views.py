from django.core.paginator import Paginator
from django.shortcuts import render
from .models import PropertyExpense, Income, Mile

def expenses(request):
    expense = PropertyExpense.objects.all()
    income = Income.objects.all()
    mile = Mile.objects.all()

    expense_paginator = Paginator(expense, 10)
    income_paginator = Paginator(income, 10)
    mile_paginator = Paginator(mile, 10)

    page_number = request.GET.get('page')
    expense_page_obj = expense_paginator.get_page(page_number)
    income_page_obj = income_paginator.get_page(page_number)
    mile_page_obj = mile_paginator.get_page(page_number)

    return render(request, 'expenses.html', {'expense_page_obj': expense_page_obj, 'income_page_obj': income_page_obj, 'mile_page_obj': mile_page_obj})