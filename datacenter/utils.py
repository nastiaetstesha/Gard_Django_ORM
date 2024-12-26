from django.utils.timezone import localtime


def get_duration(entered_local_time, leaved_local_time):
    if leaved_local_time is not None:
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


def is_visit_long(entered_local_time, leaved_local_time):
    duration = get_duration(entered_local_time, leaved_local_time)
    return duration > 3600
