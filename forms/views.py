from django.shortcuts import render

# Create your views here.
def basic_form(request):

    context = {}
    template_name = 'pages/forms/basic_form.html'
    return render(request, template_name, context)

def step_form(request):

    context = {}
    template_name = 'pages/forms/step_form.html'
    return render(request, template_name, context)

def editor_form(request):

    context = {}
    template_name = 'pages/forms/editor_form.html'
    return render(request, template_name, context)

