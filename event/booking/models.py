from django.contrib.auth.models import AbstractUser
from django.db import models
# this model is for the user event book
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'  # You can also use 'email' if you want to login using email
    REQUIRED_FIELDS = ['name', 'email', 'mobile', 'address']

    def __str__(self):
        return f"{self.username} ({self.name})"


User = get_user_model()

EVENT_TYPES = [
    ('wedding', 'Wedding'),
    ('birthday', 'Birthday'),
    ('corporate', 'Corporate Event'),
    ('social', 'Social Gathering'),
    ('other', 'Other'),
]

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    date = models.DateField()
    time = models.TimeField()
    catering = models.BooleanField(default=False)
    people_count = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_event_type_display()} for {self.user.username} on {self.date}"
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
