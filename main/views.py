from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'index.html', context={"books": books})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def shelf_view(request, category):
    books = Book.objects.filter(shelf__name__contains=category).order_by('-created_at')
    cat = category
    return render(request, 'shelf.html', context={"books": books, "category": cat})

def book_view(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book-read.html', context={"book": book})