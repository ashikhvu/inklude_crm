from rest_framework import serializers
from .models import SalePunchModel,FME_Model
# from .models import User

# class UserCreationSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = User
#         fields = "__all__"
            
class FME_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FME_Model
        fields = "__all__"

class SalePunchModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = SalePunchModel
        fields = "__all__"
        
    # sp_fme = FME_ModelSerializer()

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response["sp_fme"] = FME_ModelSerializer(instance.sp_fme).data
    #     return response