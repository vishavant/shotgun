from django.urls import path
from .views import (
    QuizCreatView,
    QuizListView,
)

from quiz import views



app_name = 'quiz'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('create-quiz', QuizCreatView.as_view(), name='create-quiz'),
    path('quiz-list',QuizListView.as_view(), name='quiz-list'),
    path('<pk>/', views.quiz_view, name='quiz-view')
]
