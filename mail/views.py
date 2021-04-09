from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def mail_inbox(request):

    context = {}
    template_name= 'pages/mails/mail_inbox.html'
    return render(request, template_name, context)


def mail_write(request):

    context = {}
    template_name= 'pages/mails/mail_write.html'
    return render(request, template_name, context)

def mail_read(request):

    context = {}
    template_name= 'pages/mails/mail_read.html'
    return render(request, template_name, context)


def contact_us(request):

    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['info@example.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/thanks/')

