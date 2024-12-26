from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.utils import get_duration, format_duration


def storage_information_view(request):
    visits_active = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits_active:
        owner_name = visit.passcard.owner_name

        entered_local_time = localtime(visit.entered_at)
        entered_at_str = entered_local_time.strftime('%d-%m-%Y %H:%M')

        leaved_local_time = None
        if visit.leaved_at is not None:
            leaved_local_time = localtime(visit.leaved_at)

        duration_seconds = get_duration(entered_local_time, leaved_local_time)
        formatted_duration = format_duration(duration_seconds)

        non_closed_visits.append({
            'who_entered': owner_name,
            'entered_at': entered_at_str,
            'duration': formatted_duration,
        })
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
