from django.urls import path
from . import views


app_name = "dashboard"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("notifications", views.notifications, name="notifications"),
    path("userprofile", views.user_profile, name="userprofile"),
    path("createEvent", views.create_event, name="createEvent"),
    path("bidForEvents", views.bid_for_events, name="bidForEvents"),
    path("hostEvents", views.host_events, name="hostEvents"),
    path("messages", views.users_message, name="messages"),

]
