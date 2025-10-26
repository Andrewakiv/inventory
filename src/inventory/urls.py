from django.urls import path
from .views import add_material_view


app_name = 'inventory'

urlpatterns = [
    path('add-material/', add_material_view, name='add_material')
]
