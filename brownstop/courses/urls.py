from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:course_id>", views.course, name="classes"),
    path("<str:course_id>/addtocal", views.addtocal, name="addtocal")
]