from django.db import models

# Create your models here.

class Question(models.Model):
    prompt = models.TextField()
    answer = models.CharField(max_length=1)

class QuizResult(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.score}/{self.total_questions} - {self.date_taken}"
