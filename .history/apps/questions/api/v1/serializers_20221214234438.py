from django.shortcuts import get_object_or_404
from rest_framework.response import Response
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

        def create(self, request, *args, **kwargs):
            movie = get_object_or_404(Movie.objects.all(), object_id=self.kwargs['movie_id'])
            for row in request.data['details']:
                row['movie'] = movie
                serializer = self.get_serializer(data=row)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)