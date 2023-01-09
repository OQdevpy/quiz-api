from django.db import models


class Questions(models.Model):
    title = models.CharField(max_length=211)

    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    questions= models.ForeignKey(Questions, null=True, blank=True,on_delete=models.CASCADE)
    anwer= models.CharField(max_length=221,null=True)

    def __str__(self):
        return self.name
    

    