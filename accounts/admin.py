from django.contrib import admin

# Register your models here.
from accounts.models import User
from accounts.managers import UserManager
from jobsapp.models import Job ,Applicant;
from accounts.managers import UserManager

admin.site.register(User)

admin.site.register(Job)
admin.site.register(Applicant)
