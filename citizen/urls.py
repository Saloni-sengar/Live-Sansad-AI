from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.citizen_dashboard, name='citizen_dashboard'),
    path('submit-complaint/', views.submit_complaint, name='submit_complaint'),
    path('my-complaints/', views.my_complaints, name='my_complaints'),
    path('complaint/<int:id>/', views.complaint_detail, name='complaint_detail'),
    path('profile/', views.citizen_profile, name='citizen_profile'),
    path('speeches/', views.citizen_speeches, name='citizen_speeches'),
]

