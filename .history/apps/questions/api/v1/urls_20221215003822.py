from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")

urlpatterns = [
    # path('list-create/', AnswerCreate.as_view()),
    path('answer-questions/', AnswerQuestionsView.as_view({'get': 'list','post': 'create'})),
]