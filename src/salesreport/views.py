from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'report.html', {'redirect_to':next})