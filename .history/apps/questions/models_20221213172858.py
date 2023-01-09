from django.db import models


class Questions(models.Model):
    title = models.CharField(max_length=211)

    created_at = models.DateTimeField(auto_now_add=True)