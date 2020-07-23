from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import *
from .serializers import *


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    permission_classes = [
        permissions.AllowAny
    ]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=id']
    ordering_fields = '__all__'


class StudentGetView(viewsets.ModelViewSet):
    serializer_class = StudentGetSerializer
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'course__id', 'studentID', 'course__period__id']

    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['=studentID']
    # ordering_fields = '__all__'


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=id']
    filterset_fields = {
        'fee': ['gte', 'lte', 'exact', 'gt', 'lt'],
    }
    ordering_fields = '__all__'


class CourseGetView(viewsets.ModelViewSet):
    serializer_class = CourseGetSerializer
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'period__id']


class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    queryset = Staff.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=id']
    ordering_fields = '__all__'


class StaffGetView(viewsets.ModelViewSet):
    serializer_class = StaffGetSerializer
    queryset = Staff.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'course__id', 'course__period__id']


class PeriodView(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=id']
    ordering_fields = '__all__'
