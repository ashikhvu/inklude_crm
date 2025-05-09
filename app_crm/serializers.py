from rest_framework import serializers
from .models import SalePunchModel
# from .models import User

# class UserCreationSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = User
#         fields = "__all__"
            
class SalePunchModelSerializer(serializers.ModelSerializer):

    # sp_fme = UserCreationSerializer()

    class Meta:
        models = SalePunchModel
        fields = "__all__"

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response["sp_fme"] = UserCreationSerializer(instance.sp_fme).data
    #     return response