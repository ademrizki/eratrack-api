from rest_framework import serializers

from api import models


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Employee
        fields = ['id', 'username', 'name',
                  'password', 'role', 'team', 'image']
        extra_kwargs = {
            'password': {
                # 'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.Employee.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            role=validated_data['role'],
            team=validated_data['team'],
            image=validated_data['image'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
