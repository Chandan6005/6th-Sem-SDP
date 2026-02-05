from django.shortcuts import render, get_object_or_404
from .models import Student
# Create your views here.

# List of all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'profiles/student_list.html', {'students': students })

# Display individual student profile
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'profiles/student_detail.html', {'student': student })