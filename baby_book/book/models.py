from django.contrib.auth.models import User
from django.db import models


class Kids(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)
    additional_info = models.TextField(blank=True)
    baby_profile_picture = models.ImageField(
        upload_to='babies',
        blank=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Memory(models.Model):
    CHOICES = (
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    )

    kid = models.ForeignKey(Kids, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    date_of_memory = models.DateField(blank=False)
    status = models.CharField(max_length=30, choices=CHOICES, blank=False)
    description = models.TextField(blank=True)
    memory_picture = models.ImageField(
        upload_to='memories',
        blank=False
    )

    def __str__(self):
        return self.title + ' from ' + str(self.date_of_memory)
