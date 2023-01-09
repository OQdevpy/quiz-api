from django.db import models
from apps.accounts.models import Account

subjects=["Math", "Pyhsics", "Algebra", "English"]



class Questions(models.Model):
    subject=models.CharField(max_length=20,choices=list(map(lambda x:(x,x),subjects)),null=True)
    title = models.CharField(max_length=211)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DayAnswerQuestions(models.Model):
    user= models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"

OPTIONS = ['a','b','c','d']

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option a')
    option_b = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option b')
    option_c = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option c')
    option_d = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option d')
    correct_answer = models.CharField(max_length=2, blank=False, null=False, choices=list(map(lambda x:(x,x),subjects)))

    def __str__(self):
        return f"{self.answer_questions.user} - {self.questions}"
    
