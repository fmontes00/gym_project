from django.core.management.base import BaseCommand, CommandError
from gym.models import Routine


class Command(BaseCommand):
    help = "count how many routines each user finish this month"

    def handle(self, *args, **kwargs):
        routines = Routine.objects.all()
        li = []
        count = 0
        for routine in routines:
            if routine.is_completed:
                count += 1
                li.append(routine.user)

        for elem in li:
            self.stdout.write(str(elem))
