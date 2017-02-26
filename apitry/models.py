from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.TextField(max_length=200)
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=0)

    class Meta:
        ordering = ('start_at',)


class Theme(models.Model):
    course_id = models.ForeignKey(Course)
    title = models.TextField(max_length=20)
    description = models.TextField(max_length=100)
    theory = models.TextField()


class UsersCourse(models.Model):
    user_id = models.ForeignKey(User)
    course_id = models.ForeignKey(Course)


class Test(models.Model):
    course_id = models.ForeignKey(Course)
    question = models.TextField()


class TestPossibleAnswers(models.Model):
    test_id = models.ForeignKey(Test)
    answer = models.TextField()
    is_true = models.BooleanField()


class TestResults(models.Model):
    user_id = models.ForeignKey(User)
    test_id = models.ForeignKey(Test)
    result = models.IntegerField(default=0)
