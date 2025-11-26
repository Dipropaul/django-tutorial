from django.urls import path,include
from . import views

urlpatterns = [   
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/',views.studentDetailView,name='student_detail'),
]