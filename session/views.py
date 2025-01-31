from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context)


def create_session(request):
    request.session['FirstSession'] = 'FirstSessionValue'
    return HttpResponse(f"<h1>{request.user}</h1>")


def get_session_value(request):
    value = request.session.get('FirstSession')
    return HttpResponse(f'<h1>{value}</h1>')


def update_session_value(request):
    request.session['FirstSession'] = 'NewSessionValue123'
    return HttpResponse(f"<h1>Yangilandi!</h1>")


def delete_session_value(request: HttpRequest):
    request.session.flush()
    return HttpResponse("<h1>O'chirildi</h1>")

