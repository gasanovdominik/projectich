from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('tenant', 'Арендатор'),
        ('landlord', 'Арендодатель'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='tenant')

    def is_tenant(self):
        return self.role == 'tenant'

    def is_landlord(self):
        return self.role == 'landlord'
