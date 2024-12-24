from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    passcard = get_object_or_404(Passcard, passcode=passcode)

    # Программируем здесь
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        entered_local_time = localtime(visit.entered_at)
        entered_at_str = entered_local_time.strftime('%d-%m-%Y %H:%M')
        
        duration_seconds = visit.get_duration()
        formatted_duration = Visit.format_duration(duration_seconds)

        is_strange = visit.is_visit_long() 
        this_passcard_visits.append({
            'entered_at': entered_at_str,
            'duration': formatted_duration,
            'is_strange': is_strange
        })
 
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
