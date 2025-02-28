from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, UserDetailsForm
from all_apps.config.models import  SystemCodeDetail


# Create your views here.
def sign_up_user(request):
    # get account type
    # account_types = SystemCodeDetail.objects.filter(system_code__name=system_codes.SC_ACCOUNT_TYPE).values('id','name')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            
            user.save()
            
            # login the user
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registration/signup.html', {'form':form})


@login_required
def user_profile(request):
    return render(request, 'useraccounts/profile.html', {'pagetitle':'My Profile', 'profile_active':'active'})


@login_required
def edit_user_details(request):
    
    # get account type
    # account_types = SystemCodeDetail.objects.filter(system_code__name=system_codes.SC_ACCOUNT_TYPE).values('id','name')
    
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            
            user.save()
            
            messages.success(request, 'Details updated successfully.')
    else:
        form = UserDetailsForm(instance=request.user)
        
    context = {
        'pagetitle':'My Profile - User Detail',
        'form': form,
        # 'account_types': account_types,
        'edit_profile_active':'active',
    }
    
    return render(request, 'useraccounts/edit/userdetails.html', context)
  
  
@login_required
def change_user_password(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            
            # update session hash once password is changed
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    
    context = {
        'pagetitle':'My Profile - Change Password',
        'form': form,
        'change_password_active':'active'
    }
    
    return render(request, 'useraccounts/edit/password.html', context)

