from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apitry.models import Course, Theme, Test, TestPossibleAnswers, TestResults, UsersCourse, Question
import time


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'course_id', 'title', 'description', 'theory')


class TestSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Test
        fields = ('id', 'course_id', 'name', 'questions')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class TestPossibleAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPossibleAnswers
        fields = ('id', 'test_id', 'answer', 'is_true')


class TestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = ('id', 'user_id', 'test_id', 'result')


class CourseSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    tests = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    start = TimestampField(source="start_at")
    finish = TimestampField(source="finish_at")
    created = TimestampField(source="created_at")

    class Meta:
        model = Course
        fields = ('id', 'start', 'finish', 'description', 'created', 'is_published', 'themes', 'tests')

