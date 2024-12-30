from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *

from django.contrib.auth import authenticate, login, logout
from .forms import CustomerSignupForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.set_password(form.cleaned_data['password'])  # Hash the password
            customer.save()

            # Log the user in after signup
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)  # Logs the user in
                return redirect('main')  # Redirect to a homepage or dashboard
            else:
                # Handle authentication error (though this should not happen since the user was just created)
                return render(request, 'Bookstore_App/signup.html', {'form': form, 'error': 'Error logging in.'})
    else:
        form = CustomerSignupForm()

    context = {'form': form}
    return render(request, 'Bookstore_App/signup.html', context)

def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('main')  # Redirects to the main page after logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Logs the user in
            return redirect('main')  # Redirects to the home page
        else:
            # Provide feedback on invalid login credentials
            return render(request, 'Bookstore_App/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Bookstore_App/login.html')



def main(request):
    return render(request, 'Bookstore_App/main.html')