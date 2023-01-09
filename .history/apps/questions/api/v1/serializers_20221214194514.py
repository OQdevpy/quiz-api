from rest_framework import serializers
from ...models import Questions,Answer




class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Questions
        fields="__all__"

class 


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Answer
        fields="__all__"

        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super(AnswerSerializer, self).create(validated_data)
