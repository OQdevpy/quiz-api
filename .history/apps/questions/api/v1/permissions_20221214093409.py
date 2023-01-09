from rest_framework import serializers
from ...models import Questions
class Questions(serializers.ModelSerializer):

    class Meta:
        model=Questions