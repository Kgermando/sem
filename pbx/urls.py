from django.urls import path

from pbx.views import cdr_view, cdr_detail

app_name = 'pbx'

urlpatterns = [
    path('appels/', cdr_view, name='cdr_view'),
    path('appels/<int:uniqueid>/', cdr_detail, name='cdr_detail'),
]

