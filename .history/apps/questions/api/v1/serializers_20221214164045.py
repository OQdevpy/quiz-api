from rest_framework import serializers
from ...models import Questions,Answer

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Answer
        fields="__all__"