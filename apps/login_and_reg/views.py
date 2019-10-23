from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User
import bcrypt

def registration_page(request):
    return render(request, 'login_and_reg/registration_page.html')

def register(request):
    print('register method is running')
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        request.session['user_id'] = user.id
        messages.success(request, "User successfully added!")
        return redirect('/wall')

def login(request):
    print("login method is running")
    user = User.objects.filter(email=request.POST['email'])
    if len(user):
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/wall')
        else:
            return redirect('/')
    else:
        return redirect('/')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')

# Create your views here.
