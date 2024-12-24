from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        entered_local_time = localtime(self.entered_at)

        if self.leaved_at is not None:  
            leaved_local_time = localtime(self.leaved_at)
            time_spent = leaved_local_time - entered_local_time
        else:
            current_time = localtime()  
            time_spent = current_time - entered_local_time  

        total_seconds = time_spent.total_seconds()
        return total_seconds

    @staticmethod
    def format_duration(duration):
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        return formatted_time
    
    def is_visit_long(self):
        duration = self.get_duration()  
        return duration > 3600
    
    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
