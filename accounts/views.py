from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError

def signupaccount(request):
  if request.method == 'GET':
    return render(request, 'signupaccount.html', {'form': UserCreateForm})
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('home')
      except IntegrityError:
        return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'That username has already been taken. Please choose a new username'})
    else:
      # Tell the user the passwords didn't match
      return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Passwords did not match'})
