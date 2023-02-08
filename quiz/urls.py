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
    path('<pk>/', views.quiz_view, name='quiz-view'),
    path('show-quizes', views.display_quiz, name='show-quizes'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('attemp-quiz', views.attemp_quiz, name='attemp-quiz'),
    path('test-result', views.test_result, name='test-result'),
]
