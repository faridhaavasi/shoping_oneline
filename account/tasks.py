from celery import shared_task
from .models import Otp
from django.utils import timezone


@shared_task()
def remov_expire_otp_code():
    expire_time = timezone.now() - timezone.timedelta(minutes=2)
    Otp.objects.filter(created__lt=expire_time).delete()
