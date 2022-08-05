from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось,с 20 раза!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
