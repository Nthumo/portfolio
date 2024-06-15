from django.urls import path
from .views import home, skills, contact_view, about, python

app_name = 'portfolio'
urlpatterns = [
    path('', home, name='home'),
    path('skills/', skills, name='skills'),
    path('prolang/python', python, name='python'),
    path('contact/', contact_view, name='contact'),
    path('about/', about, name='about'),
]