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


#class CourseSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    start_at = serializers.DateTimeField()
#    finish_at = serializers.DateTimeField()
#    description = serializers.TextField(max_length=500)
#    created_at = serializers.DateTimeField(auto_now=True)
#    is_published = serializers.BooleanField(default=0)
#
#    def create(self, validated_data):
#        return Course.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.start_at = validated_data('start_at', instance.start_at)
#        instance.finish_at = validated_data('finish_at', instance.finish_at)
#        instance.description = validated_data('description', instance.description)
#        instance.created_at = validated_data('created_at', instance.created_at)
#        instance.is_published = validated_data('is_published', instance.is_published)
#        instance.save()
#        return instance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'start_at', 'finish_at', 'description', 'created_at', 'is_published')


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id','course_id', 'title', 'description', 'theory')


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