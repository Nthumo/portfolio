from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


#contactform view
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            send_mail(
                f"New contact form submission from {name}",
                comment,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})

# home view.
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


#def intouch(request):
#    return render(request, 'portfolio/contact.html')