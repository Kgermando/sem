from django.shortcuts import render


from pbx.models import Cdr
# Create your views here.
def cdr_view(request):
    cdr_list = Cdr.objects.all().order_by('-calldate')[:10]

    context = {
         'cdr_list': cdr_list
    }
    template_name = 'pages/pbx/cdr_list.html'
    return render(request, template_name, context)


def cdr_detail(request, uniqueid):
    cdr = Cdr.objects.get(uniqueid=uniqueid)

    context = {
         'cdr': cdr
    }
    template_name = 'pages/pbx/cdr_detail.html'
    return render(request, template_name, context)

