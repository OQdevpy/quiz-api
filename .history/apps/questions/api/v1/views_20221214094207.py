from rest_framework import generics, status
from . serializers import QuestionSerializer
from ...models import Questions

class QuestionListCreate(generics.ListCreateAPIView):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()