from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Transaction, Category
from tracker.filters import TransactionFilter

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

@login_required
def transaction_list(request):
    transactions_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    )
    context = {'filter': transactions_filter}
    return render(request, 'tracker/transaction-list.html', context)