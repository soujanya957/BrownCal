from django.contrib import admin

from .models import Course, Location, Student

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
        list_display = ("c_code", "c_name", "c_loc", "c_timing")

class StudentAdmin(admin.ModelAdmin):
        filter_horizontal = ("courses", )

admin.site.register(Course, CourseAdmin)
admin.site.register(Location)
admin.site.register(Student, StudentAdmin)