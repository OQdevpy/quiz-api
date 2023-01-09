from rest_framework import generics, status,viewsets
from rest_framework.views import APIView

from apps.accounts.models import Account
from .serializers import QuestionsSerializer,AnswerQuestionsSerializer,DayAnswerQuestionsSerializer
from ...models import DayAnswerQuestions, Questions,Answer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class AnswerQuestionsView(generics.CreateAPIView):
    serializer_class=DayAnswerQuestionsSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

    def perform_create(self, serializer):
        data=self.request.data
        answer_questions=data.get('answer-questions')
        a=serializer.save(user=Account.objects.get(id=self.request.user.id))
        for i in answer_questions:
            answer=Answer.objects.create(answer=i['answer'],
                                answer_questions=a,questions=Questions.objects.get(id=i['questions']))
            answer.save()
        return Response("ok")
    

from random import randint
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    queryset=Questions.objects.all()
    def get_queryset(self):
        questions=Questions.objects.all()
        answers_questions=[j[0] for j in Answer.objects.filter(answer_questions__user=self.request.user).values_list('questions')]
        print(answers_questions)
        i=[j[0]   for j in  Questions.objects.all().values_list('id')]

        print(i)
        return super().get_queryset()
    