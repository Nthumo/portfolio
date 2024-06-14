from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')


def about(request):
    return render(request, 'portfolio/about.html')

#skills view
def skills(request):
    return render(request, 'portfolio/skills.html')

#skills sub-views
def python(request):
    return render(request, 'portfolio/python.html')


def intouch(request):
    return render(request, 'portfolio/getintouch.html')