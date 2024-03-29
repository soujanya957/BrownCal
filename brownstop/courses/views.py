from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .calendar_API import test_calendar

from courses.models import Course, Location, Student
from users.models import User

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

def tracker(request):
    return render(request, "courses/tracker.html")


def homepage(request):
    return render(request, "courses/homepage.html")

def calendar(request):
    # summary, location, description, syear, smonth, sday, eyear, emonth, eday, timezone
    if request.method == "POST":
        summary = request.POST["summary"]
        location = request.POST["location"]
        description = request.POST["description"]
        s_year = request.POST["syear"]
        s_month = request.POST["smonth"]
        s_day = request.POST["sday"]
        e_year = request.POST["eyear"]
        e_month = request.POST["emonth"]
        e_day = request.POST["eday"]
        timezone = request.POST["timezone"]

        results = test_calendar(summary, location, description, s_year, s_month, s_day, e_year, e_month, e_day, timezone)
        context = {"results": results}

        return render(request, "courses/coursecal.html", context)
    else:
        results = []
        return render(request, "courses/coursecal.html", {
            "results":results
        })
