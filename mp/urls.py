from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.mp_dashboard, name='mp_dashboard'),
    path('complaints/', views.mp_complaints, name='mp_complaints'),
    path('reply-complaint/<int:id>/', views.reply_complaint, name='reply_complaint'),
    path('speeches/', views.mp_speeches, name='mp_speeches'),
    path('add-speech/', views.add_speech, name='add_speech'),
    path('profile/', views.mp_profile, name='mp_profile'),
]

