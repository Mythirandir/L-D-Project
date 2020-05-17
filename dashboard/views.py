from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


login_required()
def dashboard(request):
    return render(request=request,
                  template_name="dashboard/dashboard.html",
                  )


login_required()
def notifications(request):
    return render(request=request,
                  template_name="dashboard/notification.html",
                  )

login_required(login_url='main:login')
def user_profile(request):
    return render(request=request,
                  template_name="dashboard/UserProfile.html",
                  )


login_required(login_url='main:login')
def users_message(request):
    return render(request=request,
                  template_name="dashboard/messages.html",
                  )


login_required(login_url='main:login')
def create_event(request):
    return render(request=request,
                  template_name="dashboard/createEvent.html",
                  )

login_required(login_url='main:login')
def host_events(request):
    return render(request=request,
                  template_name="dashboard/hostEvent.html",
                  )

login_required(login_url='main:login')
def bid_for_events(request):
    return render(request=request,
                  template_name="dashboard/bidForEvents.html",
                  )

login_required(login_url='main:login')
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect("main:login")
