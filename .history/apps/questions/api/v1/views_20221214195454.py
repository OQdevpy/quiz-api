from rest_framework import generics, status
from .serializers import QuestionsSerializer,AnswerQuestionsSerializer
from ...models import Questions,Answer
from rest_framework.permissions import IsAuthenticated


class AnswerQuestionsView(generics.CreateAPIView):
    serializer_class=AnswerQuestionsSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None


    


# class AnswerQuestionsView(generics.CreateAPIView):
#     pagination_class=None
#     queryset=Questions.objects.all()
#     serializer_class=AnswerQuestionsSerializer



