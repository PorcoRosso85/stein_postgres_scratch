from django.shortcuts import render, redirect
from django.contrib.auth import login

from .form import SignUpForm

def frontpage(request):
    return render(request, 'frontpage.html', {})

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            login(request, form.save())
            return redirect('frontpage')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
