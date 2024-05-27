from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth

from .forms import ProfileForm
# from userregistration.forms import ProfileForm
from .models import Profile


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        firstname = request.POST['First_name']
        lastname = request.POST['Last_name']
        email = request.POST['Email']
        password = request.POST['Password']
        confirm_password = request.POST['Confirm password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('userregistration:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect('userregistration:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                user.save()
                print("New User has been Created Successfully")
                messages.warning(request, 'Welcome! You have successfully registered! Please Login to your Account!!')
        else:
            messages.info(request, "Password not Matching")
            return redirect('userregistration:register')
        return redirect('userregistration:login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials ! Please Check your username or password is correct!!!")
    return render(request, 'login.html')


@login_required()
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


@login_required()
def edit_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('userregistration:view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/')
