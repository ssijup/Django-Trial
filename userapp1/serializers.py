from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['user_name' ,"user_age" ,"user_email" ,"user_password","user_entrolment_id"]

class AllUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields =['user_password' ,'user_entrolment_id']
