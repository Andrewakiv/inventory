from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from utils.transaction_helper import check_transaction
from .filters import MaterialFilter
from .forms import MaterialForm, TransactionForm
from .models import Material


def materials_view(request):
    materials = Material.objects.filter(user=request.user)
    my_filter = MaterialFilter(request.GET, queryset=materials)
    materials = my_filter.qs

    paginator = Paginator(materials, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    elided_page_range = paginator.get_elided_page_range(
        number=page_obj.number,
        on_each_side=2,
        on_ends=1
    )

    return render(request, 'inventory/materials.html',
                  {'materials': page_obj, 'page_numbers': elided_page_range})

@login_required
def add_material_view(request):
    form = MaterialForm()
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.user = request.user
            material.save()
            messages.success(request, "Material has been added")
            return redirect("inventory:materials")
    return render(request, 'inventory/add_material.html', {'form': form})


@login_required
def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(data=request.POST, request=request)
        if form.is_valid():
            try:
                check_transaction(
                    form.cleaned_data["material"],
                    form.cleaned_data["quantity"],
                    form.cleaned_data["transaction_type"],
                )
                transaction = form.save(commit=False)
                transaction.user = request.user
                transaction.save()
                messages.success(request, "Transaction has been created")
                return redirect("inventory:materials")
            except ValidationError as e:
                form.add_error(None, list(e))
    else:
        form = TransactionForm(request=request)
    return render(request, "inventory/add_transaction.html", {"form": form})
