from django.shortcuts import render
from .services import get_all_rows

# def photo_wall(request):
#   photos = get_all_rows("Test sheet")
#   return render(request, 'photo_wall.html', {'photos': photos})



from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
