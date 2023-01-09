from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})
# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# urlpatterns = router.urls

urlpatterns = [
    path('question-list/', QuestionListView.as_view()),
    path('answer/', AnswerQuestionsView.as_view()),
    path('quiz-list/', QuizListView.as_view()),
    # path('feedback/', FeedbackListView.as_view()),
    # path('statistics/',StatisticView.as_view()),
]
