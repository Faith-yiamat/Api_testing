from django.db import models
from parent.models import Parent

class Child(models.Model):
    child_id = models.PositiveSmallIntegerField(primary_key=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateTimeField()
    profile_picture = models.ImageField()
    created_at = models.DateTimeField()
    updates_at = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.gender}"

