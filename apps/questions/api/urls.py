from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.questions.api.v1.urls'))
]