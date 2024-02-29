from django.core.paginator import Paginator
from django.shortcuts import render
from .models import PropertyExpense

def expenses(request):
    # Get the order_by parameter from the request
    order_by = request.GET.get('order_by', 'payment_date')
    previous_order_by = request.session.get('order_by')

    # If the previous order_by is the same as the current order_by, then reverse the order
    if previous_order_by == order_by:
        order_by = '-' + order_by

    # Save the current order_by to the session for future use
    request.session['order_by'] = order_by

    expense = PropertyExpense.objects.order_by(order_by)

    # Pagination of the expenses table with 10 rows per page
    expense_paginator = Paginator(expense, 10)
    page_number = request.GET.get('page')
    expense_page_obj = expense_paginator.get_page(page_number)
    
    return render(request, 'expenses.html', {'expense_page_obj': expense_page_obj})