from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    # Программируем здесь
    visits_active = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits_active:
        owner_name = visit.passcard.owner_name
        non_closed_visits = []

        entered_local_time = localtime(visit.entered_at)
        entered_at_str = entered_local_time.strftime('%d-%m-%Y %H:%M')

        duration_seconds = visit.get_duration()
        formatted_duration = Visit.format_duration(duration_seconds)
        
        non_closed_visits.append({
            'who_entered': owner_name,
            'entered_at': entered_at_str,
            'duration': formatted_duration,
        })
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
