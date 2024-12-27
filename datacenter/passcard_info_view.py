from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime

from datacenter.utils import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        entered_local_time = localtime(visit.entered_at)
        entered_at_str = entered_local_time.strftime('%d-%m-%Y %H:%M')

        duration_seconds = get_duration(visit)
        formatted_duration = format_duration(duration_seconds)

        is_strange = is_visit_long(visit)
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
