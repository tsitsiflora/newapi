from rest_framework import serializers
from .models import MobileUsers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)
    designation = serializers.CharField(max_length=200)
    email = serializers.EmailField(unique=True, max_length=200)
    ec_number = serializers.IntegerField(unique=True)
    phone = serializers.PhoneNumberField(unique=True)
    centre = serializers.CharField(max_length=250)


    def create(self, validated_data):
        return MobileUsers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.email = validated_data.get('email', instance.email)
        instance.ec_number = validated_data.get('ec_number', instance.ec_number)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.centre = validated_data.get('centre', instance.centre)
