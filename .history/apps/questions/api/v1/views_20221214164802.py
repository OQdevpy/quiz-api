from rest_framework import generics, status
from . serializers import QuestionSerializer
from ...models import Questions
from rest_framework.permissions import IsAuthenticated


class QuestionListCreate(generics.ListCreateAPIView):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()
    permission_classes=[IsAuthenticated,]

    