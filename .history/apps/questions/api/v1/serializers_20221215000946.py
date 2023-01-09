from rest_framework import serializers
from ...models import DayAnswerQuestions, Questions,Answer
from rest_framework import response,status


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Questions
        fields="__all__"

class AnswerSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=Answer
        fields="__all__"

class DayAnswerQuestionsSerializer(serializers.ModelSerializer):
    questions=QuestionsSerializer(many=True,read_only=True)
    answer=AnswerSerializer(many=True,write_only=True)
    class Meta:
        model=DayAnswerQuestions
        fields="__all__"




        