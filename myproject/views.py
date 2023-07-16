from django.http import HttpResponse


# Functions defined in views.py are called `view functions`
# Creating a hello function which will display Hello World on webpage. 
def hello(request):
    return HttpResponse('Hello, World!')
