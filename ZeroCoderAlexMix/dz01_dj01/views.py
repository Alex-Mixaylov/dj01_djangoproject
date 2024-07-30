from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная страница index</h1>")

def data(request):
    return HttpResponse("<h1>Страница data</h1>")

def test(request):
    return HttpResponse("<h1>Страница test</h1>")

