from rest_framework import serializers
from ...models import Questions,Options

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Options
        fields="__all__"