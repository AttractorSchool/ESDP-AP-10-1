from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from webapp.models import Image

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        default_image = Image.objects.create(
            image='user_pic/default_user_pic.jpeg',
            user=user
        )

        user.avatar = default_image
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
