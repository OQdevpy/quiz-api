from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('list-create/', AnswerCreate.as_view()),
    path('answer-questions/', AnswerQuestionsView.as_view({'get': 'list','post': 'create'})),
]