from django.db import models

class QuizSingleAnswer(models.Model):
    question = models.CharField(max_length=255)
    choiceA = models.CharField(max_length=100)
    choiceB = models.CharField(max_length=100)
    choiceC = models.CharField(max_length=100, blank=True, null=True)
    choiceD = models.CharField(max_length=100, blank=True, null=True)
    correct = models.CharField(max_length=100)


class QuizMultiAnswer(models.Model):
    question = models.CharField(max_length=255)
    choiceA = models.CharField(max_length=100)
    choiceB = models.CharField(max_length=100)
    choiceC = models.CharField(max_length=100, blank=True, null=True)
    choiceD = models.CharField(max_length=100, blank=True, null=True)
    correct1 = models.CharField(max_length=100)
    correct2 = models.CharField(max_length=100)
    correct3 = models.CharField(max_length=100, blank=True, null=True)
    
class QuizSelectWords(models.Model):
    question = models.CharField(max_length=255)
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50, blank=True, null=True)
    choice4 = models.CharField(max_length=50, blank=True, null=True)
    choice5 = models.CharField(max_length=50, blank=True, null=True)
    choice6 = models.CharField(max_length=50, blank=True, null=True)
    choice7 = models.CharField(max_length=50, blank=True, null=True)
    choice8 = models.CharField(max_length=50, blank=True, null=True)
    correctWord1 = models.CharField(max_length=50)
    correctWord2 = models.CharField(max_length=50, blank=True, null=True)
    correctWord3 = models.CharField(max_length=50, blank=True, null=True)

class CompletedQuizes(models.Model):
    user = models.CharField(max_length=50)
    result = models.CharField(max_length=10)
    length = models.CharField(max_length=10)
    type = models.CharField(max_length=50)

