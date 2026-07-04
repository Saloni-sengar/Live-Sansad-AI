from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def citizen_register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/citizen_register.html", {
                'error': 'Username already exists. Please choose a different username.'
            })

        # Check if email already exists
        if email and User.objects.filter(email=email).exists():
            return render(request, "accounts/citizen_register.html", {
                'error': 'Email already registered. Please use a different email.'
            })

        # Check if passwords match
        if password != confirm_password:
            return render(request, "accounts/citizen_register.html", {
                'error': 'Passwords do not match. Please try again.'
            })

        # Check password length
        if len(password) < 8:
            return render(request, "accounts/citizen_register.html", {
                'error': 'Password must be at least 8 characters long.'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="citizen"
        )

        login(request,user)

        return redirect("citizen_dashboard")

    return render(request,"accounts/citizen_register.html")

def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)

            if user.role == "citizen":
                return redirect("citizen_dashboard")

            elif user.role == "mp":
                return redirect("mp_dashboard")

            else:
                return redirect("admin_dashboard")
        
        else:
            # Authentication failed - show error
            return render(request, "accounts/login.html", {
                'error': 'Invalid username or password. Please try again.'
            })

    return render(request,"accounts/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
