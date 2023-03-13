from django.contrib.auth.models import User, Group
from rest_framework import serializers
from product.models import Product


# Create your product serializer here.
"""
Solution 1
"""


class ProductSerializer(serializers.Serializer):
    # Product columns should be name , description , price , quantity and auto fileds is created and updated_at.
    pass

    def create(self, validated_data):
        # Product should be created here.
        pass

    def update(self, instance, validated_data):
        # Product should be updated here.
        pass
