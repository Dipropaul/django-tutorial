from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from staff.models import Staff
from doctor.models import Doctor
from teacher.models import Teacher
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age']
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id', 'first_name', 'last_name', 'email', 'position', 'salary']
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['staff_id', 'name', 'role', 'email']
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'name', 'specialty', 'email']
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'name', 'subject', 'email']