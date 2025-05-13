from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SalePunchModel,User
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
        serializer = SalePunchModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Sale punch created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        id=request.user.id
        user = User.objects.get(id=id)
        if user.DoesNotExist:
            print(f"\n\n{user.username}\n\n")
            if not user.is_staff:
                print("first")
                print(f"\n{type(user.username)} {user.username}")
                sp_fme,remaining = user.username.split('@')
                sp = SalePunchModel.objects.filter(sp_fme__iexact=sp_fme)
                if sp.exists():
                    serializer = SalePunchModelSerializer(sp,many=True)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                return Response({"error":"No data available"},status=status.HTTP_400_BAD_REQUEST)
            else:
                print("second")
                try:
                    sp = SalePunchModel.objects.all()
                except:
                    return Response({"error":"No data available"},status=status.HTTP_400_BAD_REQUEST)
                if sp.exists():
                    print('here')
                    serializer = SalePunchModelSerializer(sp,many=True)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                return Response({"error":"No data available"},status=status.HTTP_400_BAD_REQUEST)      
        return Response({"error":"User Does Not Exist"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,format=None):
        print(request.data.get("id"))
        id=request.data.get("id")
        print("part1")
        if not id:
            return Response({"error":"Please provide an id"},status=status.HTTP_400_BAD_REQUEST)
        try:
            sp = SalePunchModel.objects.get(id=id)
        except:
            sp=None
        
        print("part2")
        if not sp:
            return Response({"error" : "No data available right now"},status=status.HTTP_404_NOT_FOUND)
        serializer = SalePunchModelSerializer(instance=sp,data=request.data, partial=True)
        print("part3")
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return  Response({"success":"Changes Has been saved successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # return Response({"error":"Data is invalid"},status=status.HTTP_400_BAD_REQUEST)

# class SalePunchGet(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         if request.data.get("sp_fme"):
#             print(request.data.get("sp_fme"))
#         else:
#             pass
#         if request.data.get('sp_fme'):
#             sp_fme = request.data.get('sp_fme')
#             if not sp_fme:
#                 return Response({"error":"Please provide an id"},status=status.HTTP_400_BAD_REQUEST)

#             sp = SalePunchModel.objects.filter(sp_fme__iexact=sp_fme)
#             if sp.exists():
#                 serializer = SalePunchModelSerializer(instance=sp)
#                 return Response(serializer.data,status=status.HTTP_200_OK)

#             if not sp.exists():
#                 return Response({"error": "No data available right now"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             sp = SalePunchModel.objects.all()
#             serializer = SalePunchModelSerializer(sp, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
