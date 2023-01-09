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
import json
from django.http import JsonResponse
from random import randint
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    queryset=Questions.objects.all()
    def get(self,request):
        
        qs=list(Questions.objects.none())
        answers_questions=[j[0] for j in Answer.objects.filter(answer_questions__user=self.request.user).values_list('questions')]
        questions=[j[0]   for j in  Questions.objects.all().values_list('id') if j[0] not in answers_questions]
        for i in questions:
            qs.append(Questions.objects.get(id=i))

        return JsonResponse({'success': True,'qs':qs}, status=status.HTTP_200_OK)
        
    