from django.db import models

# Create your models here.
class Location(models.Model):
    l_code = models.CharField(max_length=64)
    l_room = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.l_code} {self.l_room}"

class Course(models.Model):
    c_code = models.CharField(max_length=16)
    c_name = models.CharField(max_length=64)
    c_loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="course_locations")
    c_timing = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.c_code} at {self.c_loc}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, blank=True, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Event(models.Model):
    summary = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()