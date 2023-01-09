from rest_framework import serializers
from ...models import DayAnswerQuestions, Questions,Answer
from rest_framework import response,status


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Questions
        fields="__all__"


class DayAnswerQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DayAnswerQuestions
        fields="__all__"



class AnswerQuestionsSerializer(serializers.ModelSerializer):

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

        def perform_create(self, serializer):
        # here you will send `created_by` in the `validated_data` 
            print(serializer)
            serializer.save(created_by=self.request.user)