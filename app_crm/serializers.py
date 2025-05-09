from rest_framework import serializers
from .models import SalePunchModel,FME_Model
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['username']=user.username
        token['user_type']=user.user_type
        return token

    def validate(self, attrs):
        attrs['username']=attrs.get('email')
        return super().validate(attrs)

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = "__all__"
            
class FME_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FME_Model
        fields = "__all__"

class SalePunchModelSerializer(serializers.ModelSerializer):

    sp_logo = serializers.ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = SalePunchModel
        fields = "__all__"

    # sp_fme = FME_ModelSerializer()

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response["sp_fme"] = FME_ModelSerializer(instance.sp_fme).data
    #     return response