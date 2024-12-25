from django.utils.timezone import localtime
 

def get_duration(visit):
    entered_local_time = localtime(visit.entered_at)

    if visit.leaved_at is not None:  
        leaved_local_time = localtime(visit.leaved_at)
        time_spent = leaved_local_time - entered_local_time
    else:
        current_time = localtime()  
        time_spent = current_time - entered_local_time  

    total_seconds = time_spent.total_seconds()
    return total_seconds


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
    return formatted_time
    
def is_visit_long(visit):
    duration = get_duration(visit)  
    return duration > 3600