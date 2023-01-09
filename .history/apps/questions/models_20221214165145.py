from django.db import models
from apps.accounts.models import Account

class Questions(models.Model):
    title = models.CharField(max_length=211)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    questions= models.ForeignKey(Questions, null=True, blank=True,on_delete=models.CASCADE)
    anwer= models.CharField(max_length=221,null=True)

    def __str__(self):
        return self.name
    

    