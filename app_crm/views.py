from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SalePunchModel
from .serializers import SalePunchModelSerializer,CustomTokenObtainPairSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser,JSONParser

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class SalePunchSubmit(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        serializer = SalePunchModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Sale punch created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        sp = SalePunchModel.objects.all()
        if not sp.exists():
            return Response({"error": "No data available right now"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SalePunchModelSerializer(sp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
