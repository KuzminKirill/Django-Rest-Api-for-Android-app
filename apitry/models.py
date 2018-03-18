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
    #author = models.ForeignKey(User, default='')

    class Meta:
        ordering = ('start_at',)

    def __str__(self):
        return self.name


class Theme(models.Model):
    course_id = models.ForeignKey(Course, related_name='themes', on_delete=models.CASCADE)
    title = models.TextField(max_length=20)
    description = models.TextField(max_length=100)
    theory = models.TextField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('course_id', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)


class UsersCourse(models.Model):
    user_id = models.ForeignKey(User)
    course_id = models.ForeignKey(Course)


class Test(models.Model):
    # course_id = models.ForeignKey(Course, related_name='tests', on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
    name = models.TextField()
    #author = models.ForeignKey(User, default='')
    create_date = models.DateTimeField(auto_now=True)

    #class Meta:
    #    unique_together = ('course_id', 'order')
    #    ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.name)


class Question(models.Model):
    #test_id = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=1)

    #class Meta:
    #    unique_together = ('test_id', 'order')
    #    ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.text)


class TestAnswer(models.Model):
    question_id = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, default=1)
    answer = models.TextField()
    is_true = models.BooleanField()


class TestQuestion(models.Model): # Сводная таблица
    id_test = models.ForeignKey(Test)
    id_question = models.ForeignKey(Question)


class TestResults(models.Model):
    user_id = models.ForeignKey(User)
    test_id = models.ForeignKey(Test)
    result = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='')


class Program(models.Model):
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    #author = models.ForeignKey(User, default='')
    name = models.CharField(max_length=15)


class Position(models.Model):
    id_program = models.ForeignKey(Program)


class Associate(models.Model):  # Сотрудник
    user = models.ForeignKey(User)
    position = models.ForeignKey(Position)
    fathers_name = models.CharField(max_length=20)


class CourseProgram(models.Model):
    id_course = models.ForeignKey(Course)
    id_program = models.ForeignKey(Program)


class Task(models.Model):  # Практическое задание
    name = models.CharField(max_length=15)
    text = models.CharField(max_length=200)
    #author = models.ForeignKey(User, default='')


class TaskResult(models.Model):
    id_task = models.ForeignKey(Task)
    id_associate = models.ForeignKey(Associate)
    result = models.FloatField()
    status = models.CharField(max_length=20)


class TypeZyn(models.Model):
    name = models.CharField(max_length=20)


class Specialisation(models.Model):
    name = models.CharField(max_length=20)


class ElementZyn(models.Model):
    id_type = models.ForeignKey(TypeZyn)
    id_specialisation = models.ForeignKey(Specialisation)


class PositionZyn(models.Model):
    id_zyn = models.ForeignKey(ElementZyn)
    id_position = models.ForeignKey(Position)


class AssociateProfile(models.Model):  # Профиль сотрудника
    id_associate = models.ForeignKey(Associate)
    id_zyn = models.ForeignKey(ElementZyn)


class Content(models.Model): #Контент модуля
    name = models.CharField(max_length=20)
    contain = models.FileField()
    #author = models.ForeignKey(User, default='')
    creation_date = models.DateTimeField(auto_now=True)


class Module(models.Model):
    id_test = models.ForeignKey(Test)
    id_task = models.ForeignKey(Task)
    theme = models.CharField(max_length=20)
    #author = models.ForeignKey(User, default='')


class ModuleZyn(models.Model):
    id_zyn = models.ForeignKey(ElementZyn)
    id_module = models.ForeignKey(Module)


class ModuleCourse(models.Model):
    id_course = models.ForeignKey(Course)
    id_module = models.ForeignKey(Module)


class ContentModule(models.Model): # Сводная таблица контента модуля и модуля
    id_content = models.ForeignKey(Content)
    id_module = models.ForeignKey(Module)
