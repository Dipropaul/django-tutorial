from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_list(request):
    students = [
        {'name': 'Alice', 'age': 20},
        {'name': 'Bob', 'age': 22},
    ]
    return HttpResponse(students)