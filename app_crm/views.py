from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SalePunchModel
from .serializers import SalePunchModelSerializer  # Ensure this matches your actual serializer

class SalePunchSubmit(APIView):
    
    def post(self, request):
        serializer = SalePunchModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Sale punch created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        sp = SalePunchModel.objects.all()
        if not sp.exists():
            return Response({"error": "No data available right now"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SalePunchModelSerializer(sp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
