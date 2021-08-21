from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Payment
# Create your views here.

def check_payment_successful(request):
    if Payment.status ==True:
        return HttpResponse("pardakht ba movafaghiat anjam shod")
