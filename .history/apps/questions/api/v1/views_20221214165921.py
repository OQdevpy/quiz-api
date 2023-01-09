from rest_framework import generics, status
from .serializers import QuestionsSerializer
from ...models import Questions
from rest_framework.permissions import IsAuthenticated


class AnswerCreate(generics.CreateAPIView):
    serializer_class=QuestionsSerializer
    queryset=Questions.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

