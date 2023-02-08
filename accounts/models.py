from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='student_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__(User)