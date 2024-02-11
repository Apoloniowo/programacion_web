
# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse
from django.shortcuts import render
 
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def hello_geeks (request) :
 
    # This will return Hello Geeks
    # string as HttpResponse
    return render(request, 'autores.html')