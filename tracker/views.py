from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Transaction, Category
from tracker.filters import TransactionFilter

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

@login_required
def transactions_list(request):
    transactions_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    )
    total_income = transactions_filter.qs.get_total_income()
    total_expense = transactions_filter.qs.get_total_expense()
    context = {
        'filter': transactions_filter,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_income': total_income - total_expense,
    }
    if request.htmx:
        return render(request, 'tracker/partials/transactions_container.html', context)
    return render(request, 'tracker/transaction-list.html', context)