from django.urls import path

from mail.views import mail_inbox, mail_write, mail_read, contact_us

app_name = 'mail'

urlpatterns = [
    path('mail_inbox/', mail_inbox, name='mail_inbox'),
    path('mail_write/', mail_write, name='mail_write'),
    path('mail_read/', mail_read, name='mail_read'),
    path('contact_us/', contact_us, name='contact_us'),
]
