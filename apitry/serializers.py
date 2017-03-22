from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apitry.models import Course, Theme, Test, TestPossibleAnswers, TestResults, UsersCourse


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
    class Meta:
        model = Test
        fields = ('id', 'course_id', 'question')


class TestPossibleAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPossibleAnswers
        fields = ('id', 'test_id', 'answer', 'is_true')


class TestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = ('id', 'user_id', 'test_id', 'result')


class CourseSerializer(serializers.ModelSerializer):
    themes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='theme-detail'
    )

    class Meta:
        model = Course
        fields = ('id', 'start_at', 'finish_at', 'description', 'created_at', 'is_published', 'themes')

