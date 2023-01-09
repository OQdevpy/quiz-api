from django.db import models
from apps.accounts.models import Account

class Questions(models.Model):
    title = models.CharField(max_length=211)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    questions= models.ForeignKey(Questions,on_delete=models.CASCADE,null=True)
    answer= models.TextField(null=True)
    answers= models.ForeignKey("self", on_delete=models.CASCADE)
    
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.questions}"
    

    