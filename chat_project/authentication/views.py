
from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate, login,  logout
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                # Redirect to a success page.
                return redirect('index')  # Redirect to index or any other page after successful login
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})




def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')  # Redirect to login page after logout


