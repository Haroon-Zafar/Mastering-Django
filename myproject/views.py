from django.http import HttpResponse


# Creating a hello function which will display Hello World on webpage. 
def hello(request):
    return HttpResponse('Hello World!')
