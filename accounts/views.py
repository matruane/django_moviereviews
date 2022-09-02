from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signupaccount(request):
    form = UserCreationForm()
    return render(request, 'signupaccount.html', {'form': form})
