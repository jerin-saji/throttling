from django.shortcuts import render


from rest_framework import generics
from . models import Student
from . serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework .authentication import BasicAuthentication, SessionAuthentication
from rest_framework . permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework . throttling import AnonRateThrottle,UserRateThrottle

from rest_framework . throttling import ScopedRateThrottle

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'view_stu'


# View for retrieving  student details
class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'view_stu'


# View for creating a new student
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]


# View for updating a student
class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify_stu'


# View for deleting a student
class StudentDestroyView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]


