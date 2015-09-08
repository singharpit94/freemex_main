from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app import models

# Create your views here.

def index(request):
    user=request.user
    if user.is_authenticated():
        return dashboard(request)
    return render(request, 'index_page.html', {})

def dashboard(request):
    return