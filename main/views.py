from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import NewUserForm
from .models import Blog, Category


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="main/index1.html",
                  )


def single_slug(request, single_slug):
    categories = [c.category_slug for c in Category.objects.all()]
    if single_slug in categories:
        matching_blog = Category.objects.filter(blog_category__category_slug=single_slug)
        for m in matching_blog.all():
            part_one = Blog.objects.filter(blog_category__category_slug=single_slug)
        return HttpResponse(f"(single_slug) is a category")

    blogs = [b.blog_slug for b in Blog.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"(single_slug) is a blog")

    return HttpResponse(f"(single_slug) does not correspond to anything")


def about(request):
    return render(request=request,
                  template_name="main/about.html",
                  )


def blog(request):
    context = {
        'latest': Blog.objects.order_by('-published')[0:4],
        'category': Category.objects.all(),
        'posts': Blog.objects.all()
    }
    return render(request=request,
                  template_name="main/blog.html",
                  context=context)


def contact(request):
    return render(request=request,
                  template_name="main/contact.html",
                  )


def service(request):
    return render(request=request,
                  template_name="main/service.html",
                  )


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("/login")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("dashboard:dashboard")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})
