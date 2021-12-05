from django.core.management.base import BaseCommand
from guide.models import DaysModel

# python manage.py seed --mode=refresh
from reviews.models import Tag

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
REVIEW_TAGS = ('Knowledgeable', 'Humble', 'Punctual')


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        days = [DaysModel(i) for i in DAYS]
        DaysModel.objects.bulk_create(days)
        self.stdout.write('done.')


