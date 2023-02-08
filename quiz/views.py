from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Quiz, Question

# Create your views here.



class QuizCreatView(CreateView):
    model = Quiz
    template_name = 'quiz/create_quiz.html'
    fields = '__all__'
    success_url = '/quiz-list'

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/list_quiz.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    questions = Question.objects.filter(quiz=quiz)
    
    return render(request, "quiz/quiz_view.html", {'obj':quiz, 'questions': questions,})




def homepage(request):
    return render(request, "quiz/homepage.html")



def display_quiz(request):
    return render(request, "quiz/display_quiz.html")


def leaderboard(request):
    return render(request, "quiz/leaderboard.html")


def attemp_quiz(request):
    return render(request, "quiz/attemp_quiz.html")



def test_result(request): #This will show result right after the test submission
    return render(request, "quiz/test_result.html")