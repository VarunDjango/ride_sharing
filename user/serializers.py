from rest_framework import serializers
from user.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password',
                  'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError('Both username and password are required.')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid username or password.')

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        # Add tokens to the response
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
