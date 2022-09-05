
# Create your views here.
from mysite.myapp.models import User
from django.http import HttpResponse

def index(request):
    print('start view', flush=True)
    user = User.objects.get(id=1)
    new_user = User(name='new_user', password='password')
    new_user.save()
    print('going to response', flush=True)
    return HttpResponse(user.name)