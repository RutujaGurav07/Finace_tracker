from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Transaction, Category
from tracker.filters import TransactionFilter
from tracker.forms import TransactionForm
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

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            context = {'message': "Transaction was added successfully!"}
            return render(request, 'tracker/partials/transaction-success.html', context)

    context = {'form': TransactionForm()}
    return render(request, 'tracker/partials/create-transaction.html', context)