import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Method
    def __str__(self):
        return self.question_text
    
    # timedelta defines the difference between the current time and the pub_date
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Cuando eliminar una pregunta, se eliminan todas las opciones de esa pregunta
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Mehod
    def __str__(self):
        return self.choice_text