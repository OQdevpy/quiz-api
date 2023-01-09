from rest_framework import generics, status
from . serializers import QuestionSerializer
from ...models import Question

class QuestionListCreate(generics.ListCreateAPIView):
    serializer_class=QuestionSerializer