from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.models import User

from pbx.models import Cdr, Cel, Queue
from agenda.models import Note
# Create your views here.
@login_required
def dashboard(request):
    
    user = request.user
    labels = []
    data = []

    # report CDR 
    cdr_answered = Cdr.objects.filter(lastapp='Dial').count()
    cdr_no_answer = Cdr.objects.filter(lastapp = 'HangUp').count()
    cdr_busy = Cdr.objects.filter(lastapp='Busy').count()
    cdr_total = Cdr.objects.filter().count()
    cdr_duration = Cdr.objects.all().order_by('-calldate')[:1]

    # Queue
    queue_list = Queue.objects.all().count()

    # All users
    users = User.objects.all().count()
    # Notes
    note = Note.objects.all().count()

    # Pie chart
    queryset = Cdr.objects.all()
    for cdr in queryset:
        labels.append(cdr.lastapp)
        data.append(cdr.duration)

    context = {
        'cdr_answered': cdr_answered,
        'cdr_no_answer': cdr_no_answer,
        'cdr_busy': cdr_busy,
        'cdr_total': cdr_total,
        'cdr_duration': cdr_duration,

        'queue_list' : queue_list,

        'users': users,
        'note': note,

        'labels': labels,
        'data': data,
    }
    template_name = 'pages/dashboard/dashboard.html'
    return render(request, template_name, context)



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
