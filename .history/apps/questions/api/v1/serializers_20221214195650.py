from rest_framework import serializers
from ...models import DayAnswerQuestions, Questions,Answer




class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Questions
        fields="__all__"


class DayAnswerQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DayAnswerQuestions
        fields="__all__"



class AnswerQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Answer
        fields="__all__"

        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super(AnswerQuestionsSerializer, self).create(validated_data)
