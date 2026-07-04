from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from citizen.models import Complaint
from mp.models import ParliamentSpeech

@login_required
def admin_dashboard(request):
    # Get statistics
    total_users = User.objects.count()
    total_citizens = User.objects.filter(role='citizen').count()
    total_mps = User.objects.filter(role='mp').count()
    total_admins = User.objects.filter(role='admin').count()
    total_complaints = Complaint.objects.count()
    resolved_complaints = Complaint.objects.filter(status='Resolved').count()
    pending_complaints = Complaint.objects.filter(status='Pending').count()
    total_speeches = ParliamentSpeech.objects.count()
    
    # Get recent complaints
    recent_complaints = Complaint.objects.order_by('-created_at')[:5]
    
    return render(request, "adminpanel/dashboard.html", {
        'total_users': total_users,
        'total_citizens': total_citizens,
        'total_mps': total_mps,
        'total_admins': total_admins,
        'total_complaints': total_complaints,
        'resolved_complaints': resolved_complaints,
        'pending_complaints': pending_complaints,
        'total_speeches': total_speeches,
        'recent_complaints': recent_complaints,
    })

@login_required
def manage_users(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, "adminpanel/users.html", {'users': users})

@login_required
def manage_mps(request):
    mps = User.objects.filter(role='mp').order_by('-date_joined')
    return render(request, "adminpanel/mps.html", {'mps': mps})

@login_required
def manage_complaints(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, "adminpanel/complaints.html", {'complaints': complaints})

@login_required
def manage_speeches(request):
    speeches = ParliamentSpeech.objects.all().order_by('-date')
    return render(request, "adminpanel/speeches.html", {'speeches': speeches})

