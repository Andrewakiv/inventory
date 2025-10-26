from django.shortcuts import render

from .forms import MaterialForm


def add_material_view(request):
    form = MaterialForm()
    return render(request, 'inventory/add_material.html', {'form': form})