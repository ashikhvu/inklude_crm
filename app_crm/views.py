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
from rest_framework.permissions import IsAuthenticated

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class SalePunchSubmit(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        print(request.user.id)
        serializer = SalePunchModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Sale punch created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        sp = SalePunchModel.objects.all()
        if request.POST.get('id'):
            id = request.POST.get('id')
            sp = SalePunchModel.objects.get(id=id)
            if sp:
                serializer = SalePunchModelSerializer(instance=sp)
                return Response(serializer.data,status=status.HTTP_200_OK)

        if not sp.exists():
            return Response({"error": "No data available right now"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SalePunchModelSerializer(sp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,format=None):
        id=request.POST.get(id=1)
        sp = SalePunchModel.objects.all(id=id)
        if not sp.exists():
            return Response({"error" : "No data available right now"},status=status.HTTP_404_NOT_FOUND)
        serializer = SalePunchModelSerializer(instance=sp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({"success":"Changes Has been saved successfully"},status=status.HTTP_201_CREATED)
