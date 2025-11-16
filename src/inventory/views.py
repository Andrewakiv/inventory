from dataclasses import asdict

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MaterialForm
from .models import Material


def materials_view(request):
    materials = Material.objects.all()
    return render(request, 'inventory/materials.html', {'materials': materials})

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