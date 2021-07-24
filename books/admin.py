from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

admin.site.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    list_display = [
        'answer_text',
        'is_right'
    ]

admin.site.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields =[
    'title',
    'quiz'
    ]

    list_display = [
    'title',
    'quiz'
    ]
    inlines = [AnswerInlineModel]

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
        ]
