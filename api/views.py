from django.shortcuts import render
from django.contrib.auth.models import User
from .models import QuizSingleAnswer, QuizMultiAnswer, QuizSelectWords, CompletedQuizes
from .serializer import UserSerializer, SingleAnswerSerializer, MultiAnswerSerializer, SelectWordsSerializer, CompletedQuizesSerializer, UserDetailsSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
import random




class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class QuizSingleAnswerView(generics.ListAPIView):
    serializer_class = SingleAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query_set = QuizSingleAnswer.objects.all()
        numOfQuiz = QuizSingleAnswer.objects.count()
        randomNumber = random.randint(0, numOfQuiz -1)
        randomQuiz = query_set[randomNumber : randomNumber + 1]
        return randomQuiz

class QuizMultiAnswerView(generics.ListAPIView):
    serializer_class = MultiAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query_set = QuizMultiAnswer.objects.all()
        numOfQuiz = QuizMultiAnswer.objects.count()
        randomNumber = random.randint(0, numOfQuiz -1)
        randomQuiz = query_set[randomNumber : randomNumber + 1]
        return randomQuiz
    
class QuizSelectWordsView(generics.ListAPIView):
    serializer_class = SelectWordsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query_set = QuizSelectWords.objects.all()
        numOfQuiz = QuizSelectWords.objects.count()
        randomNumber = random.randint(0, numOfQuiz -1)
        randomQuiz = query_set[randomNumber : randomNumber + 1]
        return randomQuiz


class CompletedQuizesView(generics.ListAPIView):
    serializer_class = CompletedQuizesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CompletedQuizes.objects.filter(user=user.username)


class CompletedQuizesUpdateView(generics.CreateAPIView):
    serializer_class = CompletedQuizesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = self.request.user
            serializer.save(user=user)
        else:
            print(serializer.errors)

class UsernameAndEmailView(generics.ListAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user.username) 