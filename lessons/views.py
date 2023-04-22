from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    from django.conf import settings
    return JsonResponse({
        # "var": settings.AWS_ACCESS_KEY_ID
        "var": "dasd"
    })