from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser


class User(AbstractUser):
    gender_choices=(('Male', 'Male'),('Female','Female'))
    birthday = models.DateField( null=True, blank=True)
    first_name = models.CharField( null=True, blank=True, max_length=255)
    last_name = models.CharField( null=True, blank=True, max_length=255)
    phone = models.CharField( null=True, blank=True, max_length=13)
    gender = models.CharField( null=True, blank=True, max_length=255)

    REQUIRED_FIELDS=['first_name','last_name','birthday','gender','phone']