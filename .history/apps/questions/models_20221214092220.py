from django.db import models


class Questions(models.Model):
    title = models.CharField(max_length=211)

    created_at = models.DateTimeField(auto_now_add=True)

class Options(models.Model):
    option= models.CharField(max_length=221)
    questions= models.ForeignKey(Questions, null=True, blank=True,on_delete=models.CASCADE)

    