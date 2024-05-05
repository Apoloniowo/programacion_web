
# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
 
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def hello_geeks (request) :
 
    # This will return Hello Geeks
    # string as HttpResponse
    return render(request, 'autores.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})