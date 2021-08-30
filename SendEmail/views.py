from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

#html page import required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.template import Context


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            # from_email = form.cleaned_data['from_email']
            # message = form.cleaned_data['message']
            message = "Name:" + form.cleaned_data['name'] + " " + "Email:" + form.cleaned_data['email']
            #template_name = get_template("email.html")
            try:
                send_mail("test", message, "shilpyvarshney2000@gmail.com", ['shilpyvarshney07@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #html_content = render_to_string("email.html")
            #text_content = strip_tags(html_content)
            #email = EmailMessage("test", html_content, "shilpyvarshney2000@gmail.com", ['shilpyvarshney07@gmail.com'])
            # email.attach_file(html_content, "text/html")
            # email.content_subtype = "html"
            # email.send()
            return redirect('success')
    return render(request, "email.html")


def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# Create your views here.
