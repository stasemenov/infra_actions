from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>У меня получилось!</h1>')


def second_page(request):
    return HttpResponse('А это вторая страница')
