from django.urls import path
from .views import home, skills, intouch, about, python

app_name = 'portfolio'
urlpatterns = [
    path('', home, name='home'),
    path('skills/', skills, name='skills'),
    path('prolang/python', python, name='python'),
    path('getintouch/', intouch, name='getintouch'),
    path('about/', about, name='about'),
]