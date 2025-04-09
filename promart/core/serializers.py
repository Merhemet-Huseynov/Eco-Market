from rest_framework import serializers
from .search import CustomUser

class CustomUserDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']