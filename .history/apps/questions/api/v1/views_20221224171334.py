from rest_framework import generics, status,viewsets
from rest_framework.views import APIView
from django.db.models import Count,Avg,Sum
from apps.accounts.models import Account
from .serializers import QuestionsSerializer, QuizListSerializer,QuizSerializer,AnswerQuestionsSerializer, SubjectSerializer
from ...models import Options, DayAnswerQuestions, Questions,Answer, Quiz, Subject
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# class QuestionView(generics.ListAPIView):
#     serializer_class=QuestionViewSerializer
#     permission_classes=[IsAuthenticated,]
#     queryset=Options.objects.all()
#     pagination_clas=None    


class AnswerQuestionsView(generics.CreateAPIView):
    serializer_class=AnswerQuestionsSerializer
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
                
            if answer== Options.objects.get(question__title=question.title).correct_answer:
                a.true_count+=1

            # print(question.title)
            answer=Answer.objects.create(answer=answer,
                                quiz=a,question=question)

            answer.save()
        a.save()
        return Response("ok")
        
class QuestionsListView(generics.ListAPIView):
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
        
        # data={}
        # for k, i in enumerate(qs):
        #     a = {'id': i.id, 'question': i.title}

        #     option=Options.objects.get(question__title=i.title)
        #     options=[option.option_a,option.option_b,option.option_c,option.option_d]
        #     a['options']=options
        #     data[k+1]=a
        # print(data)
        return qs.order_by('?')[:5]





class QuizListView(generics.ListAPIView):
    serializer_class=QuizListSerializer
    queryset=Quiz.objects.all()

    def get_queryset(self):
        qs=super().get_queryset()        
        qs=qs.filter(user=self.request.user)
        return qs


class SubjectView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class=SubjectSerializer
    

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
        qs=qs.values('quiz__created_at','quiz__user').annotate(quiz__true_count=Sum('quiz__true_count')).values('quiz__created_at','quiz__user', 'quiz__true_count')
        for q in qs:
            data[str(q['quiz__created_at'])]={q["quiz__user"]:{"quiz__true_count":q['quiz__true_count']}}
        return Response(data)


