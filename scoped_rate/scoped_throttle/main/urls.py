from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDestroyView,StudentRetrieveView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentRetrieveView.as_view(), name='student-retrieve'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', StudentDestroyView.as_view(), name='student-destroy'),
]
