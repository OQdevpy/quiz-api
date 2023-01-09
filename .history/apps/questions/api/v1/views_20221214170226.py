from rest_framework import generics, status
from .serializers import QuestionsSerializer
from ...models import Questions,Answer
from rest_framework.permissions import IsAuthenticated


class AnswerCreate(generics.CreateAPIView):
    serializer_class=QuestionsSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

