
import time

# Create your views here.
from mysite.myapp.models import User
from django.http import HttpResponse
from django.db import close_old_connections

def index(request):
    print('start view', flush=True)
    user = User.objects.get(id=1)
    new_user = User(name='new_user', password='password')
    new_user.save()
    print('going to response', flush=True)
    return HttpResponse(user.name)


def sleep(request, secs):
    print('start view', flush=True)
    if secs > 0:
        time.sleep(secs)
    user = User.objects.get(id=1)
    new_user = User(name='new_user', password='password')
    new_user.save()
    # close_old_connections()
    print('after ORM model', flush=True)
    if secs > 0:
        time.sleep(secs)
    print('going to response', flush=True)
    return HttpResponse(user.name)


def close_connection(request):
    print('start view', flush=True)
    user = User.objects.get(id=1)
    new_user = User(name='new_user', password='password')
    new_user.save()
    close_old_connections()
    return HttpResponse(user.name)