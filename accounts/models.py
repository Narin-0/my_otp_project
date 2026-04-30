from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class OTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # Код живет 5 минут
        return timezone.now() < self.created_at + datetime.timedelta(minutes=5)