from django.contrib.auth.models import User
from rest_framework import serializers
from .models import QuizSingleAnswer, QuizMultiAnswer, QuizSelectWords, CompletedQuizes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email",  "password"]
        extra_kwargs = {"password" : {"write_only": True}}
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        
        return user

class SingleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSingleAnswer
        fields = ["id", "question", "choiceA", "choiceB", "choiceC", "choiceD", "correct"]

class MultiAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizMultiAnswer
        fields = ["id", "question", "choiceA", "choiceB", "choiceC", "choiceD", "correct1", "correct2", "correct3"]
        
class SelectWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSelectWords
        fields = ["id", "question", "choice1", "choice2", "choice3", "choice4", "choice5", "choice6", "choice7", "choice8", "correctWord1", "correctWord2", "correctWord3"]

class CompletedQuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedQuizes
        fields = ["id", "user", "result", "length", "type"]
    


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email",]

