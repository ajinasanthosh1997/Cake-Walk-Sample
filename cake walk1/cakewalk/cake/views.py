from django.shortcuts import render, redirect
from .forms import *  # Import the form you created
from django.contrib.auth import authenticate, login
# Import your User model

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user registration data to the database
            user = form.save(commit=False)  # Create a User instance, but don't save it yet
            user.save()  # Now, save the User instance to the database
            return redirect('cake:log_in')  # Redirect to a success page

    else:
        form = UserRegistrationForm()                       

    return render(request, 'cake/signup.html', {'form': form})

# Create your views here.
def index(request):
    return render(request, 'cake/index.html')

def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cake:index')  # Redirect to the 'index' page on successful login
            else:
                # Authentication failed, display an error message to the user
                return render(request, 'cake/login.html', {'login_form': login_form, 'error_message': 'Invalid credentials'})
    else:
        login_form = LoginForm()

    return render(request, 'cake/login.html', {'login_form': login_form})

def contact(request):
    return render(request, 'cake/contact.html')   

def single(request):
    return render(request, 'cake/single-product.html')    