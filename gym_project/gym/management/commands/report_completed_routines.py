from django.core.management.base import BaseCommand, CommandError
from gym.models import Routine


class Command(BaseCommand):
    help = "count how many routines each user finish this month"

    def handle(self, *args, **kwargs):
        routines = Routine.objects.annotate()


        #my_dict = {routine.user:routine.is_completed for routine in routines}


        self.stdout.write(str(routines))
