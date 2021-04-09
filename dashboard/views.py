from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse

from pbx.models import Cdr, Cel
# Create your views here.
@login_required
def dashboard(request):
    
    user = request.user
    cdr_answered = Cdr.objects.filter(disposition = 'ANSWERED').count()-1
    cdr_no_answer = Cdr.objects.filter(disposition = 'NO ANSWER').count()
    cdr_busy = Cdr.objects.filter(disposition = 'BUSY').count()-1
    cdr_failed = Cdr.objects.filter(disposition = 'FAILED').count()
    context = {
        'cdr_answered': cdr_answered,
        'cdr_no_answer': cdr_no_answer,
        'cdr_busy': cdr_busy,
        'cdr_failed': cdr_failed,
    }
    template_name = 'pages/dashboard/dashboard.html'
    return render(request, template_name, context)


# def pie_chart(request):
#     labels = []
#     data = []

#     queryset = City.objects.order_by('-population')[:5]
#     for city in queryset:
#         labels.append(city.name)
#         data.append(city.population)

#     return render(request, 'pie_chart.html', {
#         'labels': labels,
#         'data': data,
#     })


def population_chart(request):
    labels = []
    data = []

    queryset = Cdr.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
        }
    )
