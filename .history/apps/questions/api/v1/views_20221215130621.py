from rest_framework import generics, status,viewsets
from rest_framework.views import APIView
from django.db.models import Count,Avg,Sum
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
import random
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    queryset=Questions.objects.all()
    pagination_class=None
    def get_queryset(self):
        qs=super().get_queryset()
        answers_questions=[j[0] for j in Answer.objects.filter(answer_questions__user=self.request.user).values_list('questions')]
        questions=[j[0]   for j in  Questions.objects.all().values_list('id') if j[0]  in answers_questions]
        random.shuffle(questions)
        for i in questions:
            qs=qs.exclude(id=i)
        print(questions)
        return qs.order_by('?')[:5]
    
class FeedbackListView(generics.ListAPIView):
    serializer_class = AnswerQuestionsSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

    def get_queryset(self):
        qs=super().get_queryset()
        user=self.request.user
        qs=qs.filter(answer_questions__user=user).order_by('-id')
        return qs
from pprint import pprint
class StatisticView(generics.ListAPIView):
    serializer_class = AnswerQuestionsSerializer
    queryset=Answer.objects.all()
    pagination_class=None

    def get(self,*args, **kwargs):
        data={}
        qs=super().get_queryset()
        # qs=qs.filter(answer_questions__user=self.request.user)
        qs=qs.values('answer_questions__created_at','answer_questions__user').annotate(status_ball=Sum('ball')).values('answer_questions__created_at','answer_questions__user' 'status_ball')
        pprint(qs)
        # for q in qs:
        # #     a=[{"id":i[0],"title":i[1]} for i in qs.filter(cat__title=q['cat__title']).values_list('id','title')]
        #     data[str(q['cat__title'])]={"count":q['status_count']}
        
        return Response(qs)