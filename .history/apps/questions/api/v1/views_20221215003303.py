from rest_framework import generics, status,viewsets
from .serializers import QuestionsSerializer,AnswerQuestionsSerializer,DayAnswerQuestionsSerializer
from ...models import Questions,Answer
from rest_framework.permissions import IsAuthenticated


class AnswerQuestionsView(viewsets.ViewSet):
    serializer_class=DayAnswerQuestionsSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

    def perform_create(self, serializer):
        print(1)
        return super().perform_create(serializer)
    


# class AnswerQuestionsView(generics.CreateAPIView):
#     pagination_class=None
#     queryset=Questions.objects.all()
#     serializer_class=AnswerQuestionsSerializer



