from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'))


YEAR_CHOICES = (
    ('First', 'First Year'),
    ('Second', 'Second Year'),
    ('Third', 'Third Year'),
    ('Fourth', 'Fourth Year'),
    ('M1st', 'M.Tech First Year'),
    ('M2nd', 'M.Tech Second Year'),
    ('phd', 'PHD'))


Dept_Choices = (
	('cse','CSE'),
	('ee','EE'),
	('ece','ECE'),
	('me','ME'),
	('mme','MME'),
	('ce','CE'))






class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="Other",choices= GENDER_CHOICES )
    YearofStudy = models.CharField(max_length=20, default="First Year" , choices= YEAR_CHOICES)
    RegNo = models.CharField(max_length=9, default="12u10888")
    Dept = models.CharField(max_length=9, default="CSE",choices= Dept_Choices)
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
