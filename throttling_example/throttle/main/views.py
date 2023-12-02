from django.shortcuts import render


from rest_framework import generics
from . models import Student
from . serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework .authentication import BasicAuthentication, SessionAuthentication
from rest_framework . permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework . throttling import AnonRateThrottle,UserRateThrottle

from . throttling import CustomRateThrottle

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,CustomRateThrottle]

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,CustomRateThrottle]

