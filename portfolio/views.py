from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import logging


logger = logging.getLogger(__name__)

#contactform view
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            try:
                send_mail(
                    f"New contact form submission from {name}",
                    comment,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                return redirect('contact')
            except Exception as e:
                logger.error(f"Error Sending Email: {e}")
                return render(request, 'portfolio/contact.html', {'form':form, 'error': 'There was an error sending your message. Please try later.'})
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