from rest_framework import generics, status
from . serializers import QuestionSerializer
from ...models import Questions

class QuestionListCreate(generics.ListAPIView):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()