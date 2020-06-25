from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.image import Image
from .models.user import User
from .models.house import House
from .models.booking import Booking

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Booking
      fields = ('__all__')

class HouseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)
    class Meta:
      model = House
      fields = ('id', 'name', 'description', 'city', 'country', 'price', 'images', 'amenities', 'bookings', 'longitude', 'latitude')

class BookingReadSerializer(BookingSerializer):
    property = HouseSerializer(read_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
