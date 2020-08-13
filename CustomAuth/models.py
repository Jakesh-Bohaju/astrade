from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from DecorFront.validator import phone_no_validation, mobile_no_validation


class Profile(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    phone_no1 = models.CharField(max_length=10, validators=[mobile_no_validation], blank=True, null=True)
    phone_no2 = models.CharField(max_length=10, validators=[mobile_no_validation], blank=True, null=True)


