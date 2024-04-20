from django.contrib import admin
from .models import QuizMultiAnswer, QuizSelectWords, QuizSingleAnswer, CompletedQuizes

admin.site.register(QuizSingleAnswer)

admin.site.register(QuizMultiAnswer)

admin.site.register(QuizSelectWords)

admin.site.register(CompletedQuizes)


# Register your models here.
