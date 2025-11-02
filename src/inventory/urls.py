from django.urls import path
from .views import add_material_view, materials_view


app_name = 'inventory'

urlpatterns = [
    path('add-material/', add_material_view, name='add_material'),
    path('materials/', materials_view, name='materials')
]
