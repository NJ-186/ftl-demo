
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from random import randint
from datetime import timedelta, datetime

from core.models import USER, ActivityPeriod


class Command(BaseCommand):
    help = 'Populates the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default = 10,
            type = int ,
            help = 'The number of fake USERs to create.')

        parser.add_argument('--time',
            default = 10,
            type = int ,
            help = 'The number of time periods to create.')


    def handle(self, *args, **options):
        if options['users']:
            for _ in range(options['users']):
                USER.objects.create(
                    id = str(get_random_string(length = 9)),
                    real_name = str(get_random_string( length = 20)),
                    tz = str(get_random_string(length = 30)),
                )
        
        if options['time']:
            USER_count = USER.objects.all().count()

            for _ in range(options['time']):
                ActivityPeriod.objects.create(
                    user = USER.objects.all()[randint(0 , USER_count - 1)],
                    start_time = datetime.now() - timedelta(seconds = randint(0, 86400)),
                    end_time = datetime.now() + timedelta(seconds = randint(0, 86400))
                )