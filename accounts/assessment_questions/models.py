from django.db import models
from milestone.models import Milestone
# from .models import Assessment

class Assessment(models.Model):
    question_id = models.PositiveSmallIntegerField(primary_key=True)
    milestone_id = models.ForeignKey(Milestone, on_delete=models.CASCADE, default=1)
    question = models.CharField(max_length= 80)
    question_type = models.CharField(max_length= 20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    def __str__ (self):
        return f"{self.question} {self.created_at}"
    