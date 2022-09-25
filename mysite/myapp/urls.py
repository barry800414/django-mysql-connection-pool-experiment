from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sleep/<int:secs>', views.sleep, name='sleep'),
    path('close/', views.close_connection, name='close_connection'),

]