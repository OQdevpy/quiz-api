from django.urls import path, include
from .views import *

urlpatterns = [
    path('list-create/', QuestionListCreate.as_view()),
]