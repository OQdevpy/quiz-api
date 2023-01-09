from rest_framework import generics, status,viewsets
from rest_framework.views import APIView
from django.db.models import Count,Avg,Sum
from apps.accounts.models import Account
from .serializers import QuestionsSerializer,QuizSerializer,DayAnswerQuestionsSerializer
from ...models import Options, DayAnswerQuestions, Questions,Answer, Quiz
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
            # print(Answer.objects.get(question=i['question']))
            # print(i['question'])
            # if i['question'] in Answer.objects.get(question__id=i['question']):
            #     return Response('Already answer')
            answer=i['answer']
            question=Questions.objects.get(id=i['question'])
            true_answer=Options.objects.get(question=question)
            # print(true_answer)
            print(question)
            answer=Answer.objects.create(answer=answer,
                                quiz=a,question=question)

            answer.save()
        return Response("ok")
        
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    queryset=Questions.objects.all()
    pagination_class=None

    def get_queryset(self):
        qs=super().get_queryset()        
        subject=self.request.GET.get('subject')
        qs=qs.filter(subject=subject.title())
        answers_questions=[j[0] for j in Answer.objects.filter(quiz__user=self.request.user).values_list('question')]
        questions=[j[0]   for j in  Questions.objects.filter(subject=subject).values_list('id') if j[0]  in answers_questions]
        for i in questions:
            qs=qs.exclude(id=i)
        return qs.order_by('?')[:5]
    
class FeedbackListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

    def get_queryset(self):
        qs=super().get_queryset()
        user=self.request.user
        qs=qs.filter(answer_questions__user=user).order_by('-id')
        return qs

class StatisticView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset=Answer.objects.all()
    pagination_class=None

    def get(self,*args, **kwargs):
        # sourcery skip: dict-comprehension, move-assign-in-block
        data={}
        qs=super().get_queryset()
        qs=qs.values('answer_questions__created_at','answer_questions__user').annotate(status_ball=Sum('ball')).values('answer_questions__created_at','answer_questions__user', 'status_ball')
        for q in qs:
            data[str(q['answer_questions__created_at'])]={q["answer_questions__user"]:{"ball":q['status_ball']}}
        return Response(data)