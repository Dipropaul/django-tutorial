from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('teachers', views.TeacherViewSet, basename='teacher')

urlpatterns = [   
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/',views.studentDetailView,name='student_detail'),
    #class based view
    path('employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/',views.EmployeeDetailView.as_view(),name='employee_detail'),
    
    path('staff/', views.StaffList.as_view(), name='staff_list'),
    path('staff/<int:pk>/',views.StaffDetailView.as_view(),name='staff_detail'),
    
    path('doctors/', views.DoctorList.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/',views.DoctorDetailView.as_view(),name='doctor_detail'),
    
    path('', include(router.urls)),
    path('blogs/', views.BlogList.as_view(), name='blog_list'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
]