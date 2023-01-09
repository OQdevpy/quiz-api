from django.db import models
from apps.accounts.models import Account

subjects=["Math", "Pyhsics", "Algebra", "English"]



class Questions(models.Model):
    subject=models.CharField(max_length=20,choices=list(map(lambda x:(x,x),subjects)),null=True)
    title = models.CharField(max_length=211)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

OPTIONS = ['A','B','C','D']
class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option A')
    option_b = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option B')
    option_c = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option C')
    option_d = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option D')
    correct_answer = models.CharField(max_length=2, blank=False, null=False, choices=list(map(lambda x:(x,x),OPTIONS)))

    def __str__(self) -> str:
        return self.question.title

class Quiz(models.Model):
    user= models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    
class Answer(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE,null=True)
    answer = models.CharField(max_length=2, blank=False, null=False, choices=list(map(lambda x:(x,x),OPTIONS)))
    created_at = models.DateTimeField(auto_now_add=True)
    correctness=models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    

class DayAnswerQuestions(models.Model):
    user= models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"


# class Answer(models.Model):
#     answer_questions=models.ForeignKey(DayAnswerQuestions,on_delete=models.CASCADE,null=True)
#     questions= models.ForeignKey(Questions,on_delete=models.CASCADE)
#     ball= models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=0)
#     answer= models.TextField(null=True)
#     feedback= models.TextField(null=True,blank=True)
#     created_at= models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.answer_questions.user} - {self.questions}"
    
