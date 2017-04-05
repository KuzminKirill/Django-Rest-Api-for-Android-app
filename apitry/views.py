from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apitry.serializers import UserSerializer, GroupSerializer
from apitry.models import Course, Test, Theme, Question
from apitry.serializers import CourseSerializer, TestSerializer, ThemeSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


#class UserDetail(generics.RetrieveAPIView):
#    model = User
#    serializer_class = UserSerializer
#    lookup_field = 'username'

#@api_view(['GET', 'POST'])
#def course_list(request, format=None):
#    """
#    List all courses, or create a new course.
#    """
#    if request.method == 'GET':
#        courses = Course.objects.all()
#        serializer = CourseSerializer(courses, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = CourseSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET', 'PUT', 'DELETE'])
#def course_detail(request, pk, format=None):
#    """
#    Retrieve, update or delete a course instance.
#    """
#    try:
#        course = Course.objects.get(pk=pk)
#    except Course.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = CourseSerializer(course)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        serializer = CourseSerializer(course, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        course.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

