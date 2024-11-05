from django.db import models
from users.models import User

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()            # описание
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.IntegerField()
    housing_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')      # владелец

    def __str__(self):
        return self.title