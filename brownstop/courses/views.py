from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Course, Location, Student

# Create your views here.
def index(request):
    return render(request, "courses/index.html",{
        "courses": Course.objects.all()
    })

def course(request, course_id):
    course = Course.objects.get(c_code=course_id)
    return render(request, "courses/course.html", {
        "course": course,
        "students": course.students.all(),
        "non_students": Student.objects.exclude(courses=course).all()
    })

def addtocal(request, course_id): 
    if request.method == "POST":
        course = Course.objects.get(c_code=course_id)
        student = Student.objects.get(pk=str(request.POST["student"]))
        student.courses.add(course)

        return HttpResponseRedirect(reverse("classes", args=(course_id,)))

