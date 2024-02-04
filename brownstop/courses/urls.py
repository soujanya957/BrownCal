from django.urls import path

from . import views
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView, GoogleCalendarEventsView

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:course_id>", views.course, name="classes"),
    path("<str:course_id>/addtocal", views.addtocal, name="addtocal"),
    path("degreetracker/", views.tracker, name="tracker"),
    path("home/", views.homepage, name="homepage"),
    path("coursecalendar/", views.calendar, name="calendar"),
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='calendar_init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='calendar_redirect'),
    path('rest/v1/calendar/events/', GoogleCalendarEventsView.as_view(), name='calendar_redirect'),
]