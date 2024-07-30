from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная страница index</h1>")

def new(request):
    return HttpResponse("<h1>Страница new</h1>")

