from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    userId = serializers.CharField(max_length=10)
    time = serializers.CharField(max_length=10)
    sign = serializers.CharField(max_length=10)

class SendAlarmSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    accessToken = serializers.CharField(max_length=10)
    deviceCode = serializers.CharField(max_length=10)
    warningList = serializers.CharField(max_length=10)
    alarmId = serializers.CharField(max_length=10)
    alarmTime = serializers.CharField(max_length=10)

class SendFaultSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    accessToken = serializers.CharField(max_length=10)
    deviceCode = serializers.CharField(max_length=10)
    faultList = serializers.CharField(max_length=10)
    faultCode = serializers.CharField(max_length=10)
    faultTime = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
