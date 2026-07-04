
from django.shortcuts import render, redirect, get_object_or_404
from citizen.models import Complaint
from .models import ParliamentSpeech
from django.contrib.auth.decorators import login_required

@login_required
def mp_dashboard(request):
    complaints = Complaint.objects.all().order_by('-created_at')[:10]
    
    # Get statistics
    total_complaints = Complaint.objects.count()
    pending_complaints = Complaint.objects.filter(status="Pending").count()
    resolved_complaints = Complaint.objects.filter(status="Resolved").count()
    
    # Get MP's speeches
    total_speeches = ParliamentSpeech.objects.filter(mp=request.user).count()
    
    # Get recent speeches
    speeches = ParliamentSpeech.objects.filter(mp=request.user).order_by('-date')[:3]
    
    return render(request, "mp/dashboard.html", {
        'complaints': complaints,
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'resolved_complaints': resolved_complaints,
        'total_speeches': total_speeches,
        'speeches': speeches,
    })

@login_required
def reply_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    
    if request.method == "POST":
        complaint.mp_reply = request.POST.get('reply', '')
        status = request.POST.get('status', 'Pending')
        complaint.status = status
        complaint.save()
        return redirect("mp_complaints")
    
    return render(request, "mp/reply_complaint.html", {'complaint': complaint})

@login_required
def mp_complaints(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, "mp/complaints.html", {'complaints': complaints})

@login_required
def mp_speeches(request):
    speeches = ParliamentSpeech.objects.filter(mp=request.user).order_by('-date')
    return render(request, "mp/speeches.html", {'speeches': speeches})

@login_required
def add_speech(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        speech_text = request.POST.get('speech_text', '')
        summary = request.POST.get('summary', '')
        
        ParliamentSpeech.objects.create(
            mp=request.user,
            title=title,
            speech_text=speech_text,
            summary=summary
        )
        return redirect("mp_speeches")
    
    # Get recent speeches
    recent_speeches = ParliamentSpeech.objects.filter(mp=request.user).order_by('-date')[:3]
    
    return render(request, "mp/add_speech.html", {
        'recent_speeches': recent_speeches
    })

@login_required
def mp_profile(request):
    complaints = Complaint.objects.all()
    resolved_complaints = complaints.filter(status="Resolved").count()
    total_complaints = complaints.count()
    total_speeches = ParliamentSpeech.objects.filter(mp=request.user).count()
    
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        return redirect('mp_profile')
    
    return render(request, "mp/profile.html", {
        'resolved_complaints': resolved_complaints,
        'total_complaints': total_complaints,
        'total_speeches': total_speeches,
    })

