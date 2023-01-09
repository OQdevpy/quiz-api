from django.urls import path, include
from .views import *
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    # path('list-create/', AnswerCreate.as_view()),
    path('answer-questions/', AnswerQuestionsView.as_view()),
]