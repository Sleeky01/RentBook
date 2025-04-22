from django.urls import path
from . import views

urlpatterns = [
    path('', views.rentbook_list, name='rentbook_list'),
    path('add/', views.rentbook_create, name='rentbook_create'),
    path('edit/<int:pk>/', views.rentbook_edit, name='rentbook_edit'),
    path('delete/<int:pk>/', views.rentbook_delete, name='rentbook_delete'),
]
