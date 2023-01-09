from rest_framework import generics, status,viewsets
from rest_framework.views import APIView
from .serializers import QuestionsSerializer,AnswerQuestionsSerializer,DayAnswerQuestionsSerializer
from ...models import Questions,Answer
from rest_framework.permissions import IsAuthenticated


class AnswerQuestionsView(APIView):
    serializer_class=DayAnswerQuestionsSerializer
    queryset=Answer.objects.all()
    permission_classes=[IsAuthenticated,]
    pagination_class=None

    # def perform_create(self, serializer):
    #     print(1)
    #     return super().perform_create(serializer)
    


# class AnswerQuestionsView(generics.CreateAPIView):
#     pagination_class=None
#     queryset=Questions.objects.all()
#     serializer_class=AnswerQuestionsSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = AnswerQuestionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AnswerQuestionsSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer= AnswerQuestionsSerializer
        queryset=Answer.objects.all()

        return Response(serializer.data)


