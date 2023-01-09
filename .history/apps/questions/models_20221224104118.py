from django.db import models
from apps.accounts.models import Account

subjects=["Math", "Pyhsics", "Algebra", "English"]



class Questions(models.Model):
    title = models.CharField(max_length=211)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DayAnswerQuestions(models.Model):
    user= models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"


class Answer(models.Model):
    answer_questions=models.ForeignKey(DayAnswerQuestions,on_delete=models.CASCADE,null=True)
    questions= models.ForeignKey(Questions,on_delete=models.CASCADE)
    ball= models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=0)
    answer= models.TextField(null=True)
    feedback= models.TextField(null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.answer_questions.user} - {self.questions}"
    
