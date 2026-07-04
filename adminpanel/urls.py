
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.manage_users, name='manage_users'),
    path('mps/', views.manage_mps, name='manage_mps'),
    path('complaints/', views.manage_complaints, name='manage_complaints'),
    path('speeches/', views.manage_speeches, name='manage_speeches'),
]

