from django.db import models
from child.models import Child

class Milestone(models.Model):
    milestone_id = models.PositiveSmallIntegerField(primary_key=True)
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length= 20)

    def __str__(self):
        return f"{self.milestone_id} {self.status}"