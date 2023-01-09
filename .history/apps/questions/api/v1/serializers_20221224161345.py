from rest_framework import serializers
from ...models import DayAnswerQuestions, Questions,Answer, Quiz
from rest_framework import response,status


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Questions
        fields="__all__"




    
# class QuestionViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Options
        
class QuizSerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField(read_only=True)

    # def get_children(self, obj):
    #     try:
    #         comments = Questions.objects.all()
    #     except:
    #         return []
    #     else:
    #         serializer = DayAnswerQuestionsSerializer(comments, many=True)
    #         return serializer.data

    class Meta:
        model=Answer
        fields="__all__"

class AnswerQuestionsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Quiz
        fields="__all__"


class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Quiz
        fields="__all__"





        