from django.db import models
from users.models import User

class Doctor(models.Model):
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctors')
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



