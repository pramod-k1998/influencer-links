from django.db import models
import random
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Category(models.Model):
    """
    Represents a product category (e.g., Tech, Beauty, etc.)
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class ProductLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class AdminOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() < self.created_at + timedelta(minutes=5)