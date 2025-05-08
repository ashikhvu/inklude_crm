from rest_framework import serializers
from .models import User

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = "__all__"
            
