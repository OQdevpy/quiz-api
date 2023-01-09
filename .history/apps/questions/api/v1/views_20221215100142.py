from rest_framework import generics, status,viewsets
from rest_framework.views import APIView

from apps.accounts.models import Account
from .serializers import QuestionsSerializer,AnswerQuestionsSerializer,DayAnswerQuestionsSerializer
from ...models import Questions,Answer
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
            print(i['questions'])
            answer=Answer.objects.create(ball=i['ball'],answer=i['answer'],feedback=i['feedback'],
                                answer_questions=a,questions=Questions.objects.get(id=i['questions']))
            answer.save()
        return Response("ok")
    


# class AnswerQuestionsView(generics.CreateAPIView):
#     pagination_class=None
#     queryset=Questions.objects.all()
#     serializer_class=AnswerQuestionsSerializer
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from rest_framework.response import Response

# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Answer.objects.all()
#         serializer = AnswerQuestionsSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Answer.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = AnswerQuestionsSerializer(user)
#         return Response(serializer.data)

#     def create(self, request):
#         print(request)
#         queryset=Answer.objects.all()
#         serializer= AnswerQuestionsSerializer(queryset)

#         return Response(serializer.data)


