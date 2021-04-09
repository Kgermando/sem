from django.urls import path

from forms.views import basic_form, step_form, editor_form

app_name = 'forms'

urlpatterns = [
    path('forms/basic_form/', basic_form, name='basic_form'),
    path('forms/step_form/', step_form, name='step_form'),
    path('forms/editor_form/', editor_form, name='editor_form'),
]
