from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PasswordResetRequest
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import CustomUser
# Create your views here.
# User = get_user_model()
# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         role_from = request.POST.get('role')

      
#         user = User.objects.create_user(
#             username=email,
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             role=role_from
            
#         )
#         if role_from == 'student':
#             user.is_student = True
#         elif role_from == 'teacher':
#             user.is_teacher = True
#         elif role_from == 'admin':
#             user.is_admin = True
#         user.save()
#         login(request, user)


#         messages.success(request, 'Registration successful. You can now log in.')

#         return redirect('home')

#     return render(request, 'authorization/signup.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role') 
        
        # Create the user
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        
       
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True

        user.save()  
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('dashborad') 
    return render(request, 'authentication/signup.html')  



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')

            
            if user.is_admin:
                return redirect('admin_dashdoard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('student_dashboard')
            
            else:
                messages.error(request, 'Invalid email or password.')
                return redirect('index')
            

            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')



    return render(request, 'authentication/login.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = get_random_string(length=32)
            rest_request = PasswordResetRequest.objects.create(user=user, token=token)
            rest_request.send_reset_email()
            messages.success(request, 'Password reset email sent successfully.')
            return redirect('index')
        else:   
            messages.error(request, 'Email not found.')
            return redirect('index')
        

    return render(request, 'authentication/forgot_password.html')


def reset_view(request, token):

    reset_request = PasswordResetRequest.objects.filter(token=token).first()
    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Password reset link is invalid or has expired.')

        return redirect('index')
    

    if request.method == 'POST':
        new_password = request.POST.get('password')
        user = reset_request.user
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password reset successful. You can now log in.')
        return redirect('login')
    
    return render(request, 'authentication/reset_password.html',{'token': token})



def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')

        