from django.shortcuts import render
from django.http import HttpResponse

menu = [
    {'title': 'chiqish', 'url_name': 'about'},
    {'title': 'malumotlarni korish', 'url_name': 'addpage'},
    {'title': 'list kiritish', 'url_name': 'contact'},
    {'title': 'royxatdan otish', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'name': 'sardor shukurov', 'yoshi': 21},
    {'id': 2, 'name': 'akmal omonturdiyev', 'yoshi': 24},
    {'id': 3, 'name': 'mahfuza omonturdiyeva', 'yoshi': 18}
]


def index(request):
    data = {
        'title': 'Bosh menyuga xush kelibsiz',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'web1/index.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f'id:{post_id} ga teng bolgan listga xush kelibsiz')


def about(request):
    return HttpResponse('url aboutga teng bolgan listga xush kelibsiz')


def addpage(request):
    return HttpResponse('url addpagega teng bolgan listga xush kelibsiz')


def contact(request):
    return HttpResponse('url contactga teng bolgan listga xush kelibsiz')


def login(request):
    return HttpResponse('url loginga teng bolgan listga xush kelibsiz')
