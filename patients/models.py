from django.db import models
from users.models import User

class Patient(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
        ("Prefer not to say", "Prefer not to say")
    ]
    added_by= models.ForeignKey(User, on_delete=models.CASCADE,related_name='patients')
    first_name= models.CharField(max_length=100, blank=False)
    last_name= models.CharField(max_length=100, blank=False)
    age=models.PositiveIntegerField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES, default="Prefer not to say")

    def __str__(self):
        return f"{self.last_name} added by {self.added_by}"
