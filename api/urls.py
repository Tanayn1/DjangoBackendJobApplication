from django.urls import path
from .views import QuizSingleAnswerView, QuizMultiAnswerView, QuizSelectWordsView, CompletedQuizesUpdateView, CompletedQuizesView, UsernameAndEmailView

urlpatterns = [
    path('getQuiz/singlechoice/', QuizSingleAnswerView.as_view(), name="Single-Quiz" ),
    path('getQuiz/multichoice/', QuizMultiAnswerView.as_view(), name='Multi-Quiz'),
    path('getQuiz/selectwords/', QuizSelectWordsView.as_view(), name='Select-Words'),
    path('getQuiz/updatequizes/', CompletedQuizesUpdateView.as_view(), name='Update-Quizes'),
    path('getQuiz/showquizes/', CompletedQuizesView.as_view(), name='Show-Quizes' ),
    path('user/fetchuser/', UsernameAndEmailView.as_view(), name='fetch-user')
]