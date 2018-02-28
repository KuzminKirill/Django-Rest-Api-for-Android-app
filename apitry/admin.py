from django.contrib import admin
from .models import Course, Theme, Test, Question, TestPossibleAnswers

# Register your models here.
admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestPossibleAnswers)
