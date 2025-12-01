from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from .filters import MaterialFilter
from .forms import MaterialForm
from .models import Material


def materials_view(request):
    materials = Material.objects.all()
    my_filter = MaterialFilter(request.GET, queryset=materials)
    materials = my_filter.qs

    paginator = Paginator(materials, 1)
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
            material.save()
            messages.success(request, "Material has been added")
            return redirect("inventory:materials")
    return render(request, 'inventory/add_material.html', {'form': form})