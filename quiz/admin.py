from django.contrib import admin
from .models import *


# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer



class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['quiz', 'text']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(QuizLevel)
admin.site.register(Quiz)
admin.site.register(Result)