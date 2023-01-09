from django.urls import path, include
from .views import *

urlpatterns = [
    path('list-create/', AnswerCreate.as_view()),
    path('questions/', AnswerCreate.as_view()),
]