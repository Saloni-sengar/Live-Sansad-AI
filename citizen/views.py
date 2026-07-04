from django.shortcuts import render, redirect, get_object_or_404
from .models import Complaint
from mp.models import ParliamentSpeech
from django.contrib.auth.decorators import login_required

@login_required
def citizen_dashboard(request):
    complaints = Complaint.objects.filter(citizen=request.user)
    
    # Get statistics
    total_complaints = complaints.count()
    pending_complaints = complaints.filter(status="Pending").count()
    in_progress_complaints = complaints.filter(status="In Progress").count()
    resolved_complaints = complaints.filter(status="Resolved").count()
    
    # Get recent complaints
    recent_complaints = complaints.order_by('-created_at')[:5]
    
    # Get latest speeches
    latest_speeches = ParliamentSpeech.objects.order_by('-date')[:3]
    
    return render(request, "citizen/dashboard.html", {
        'complaints': recent_complaints,
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'in_progress_complaints': in_progress_complaints,
        'resolved_complaints': resolved_complaints,
        'latest_speeches': latest_speeches,
    })

@login_required
def submit_complaint(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']

        Complaint.objects.create(
            citizen=request.user,
            title=title,
            description=description,
            category=category
        )

    # Get recent complaints for sidebar
    recent_complaints = Complaint.objects.filter(citizen=request.user).order_by('-created_at')[:3]
    
    return render(request, "citizen/submit_complaint.html", {
        'recent_complaints': recent_complaints
    })

@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(citizen=request.user).order_by('-created_at')
    return render(request, "citizen/my_complaints.html", {'complaints': complaints})

@login_required
def complaint_detail(request, id):
    complaint = get_object_or_404(Complaint, id=id, citizen=request.user)
    return render(request, "citizen/complaint_detail.html", {'complaint': complaint})

@login_required
def citizen_profile(request):
    complaints = Complaint.objects.filter(citizen=request.user)
    total_complaints = complaints.count()
    resolved_complaints = complaints.filter(status="Resolved").count()
    pending_complaints = complaints.filter(status="Pending").count()
    
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        return redirect('citizen_profile')
    
    return render(request, "citizen/profile.html", {
        'total_complaints': total_complaints,
        'resolved_complaints': resolved_complaints,
        'pending_complaints': pending_complaints,
    })

@login_required
def citizen_speeches(request):
    speeches = ParliamentSpeech.objects.all().order_by('-date')
    
    # Get list of MPs for filter
    mps = []
    for speech in speeches:
        if speech.mp not in mps:
            mps.append(speech.mp)
    
    return render(request, "citizen/speeches.html", {
        'speeches': speeches,
        'mps': mps,
    })
