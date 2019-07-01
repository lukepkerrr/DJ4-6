from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(
        request,
        'registration/signup.html',
        {'form': form}
    )

def logout_result(request):
    return render(
        request,
        'registration/logout_result.html'
    )