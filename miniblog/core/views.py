from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenidos a todos")

def about(request):
    return HttpResponse("Acerca de")