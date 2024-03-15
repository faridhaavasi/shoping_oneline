from django.core.management.base import BaseCommand, CommandError
from account.models import Otp
from django.utils import timezone


class Command(BaseCommand):
    help = 'delete otp code is expired time'

    def handle(self, *args, **options):
        expire_time = timezone.now() - timezone.timedelta(minutes=2)
        Otp.objects.filter(created__lt=expire_time).delete()

        self.stdout.write('deleted expire time otp')
