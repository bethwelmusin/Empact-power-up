from rest_framework import serializers
from django.contrib.auth import get_user_model
from authentication.models import EmpactUser




User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']
		read_only_fields = ['id']
      
class EmpactUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmpactUser
		fields = ['id', 'first_name','last_name','mobile_number', 'email', 'user_type','member_type', 'date_created','updated_on' ]
		read_only_fields = ['id']
      

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    mobile_no = serializers.CharField()
    email = serializers.CharField()
    user_type = serializers.CharField()
    member_type = serializers.CharField()
    profile_pic_url = serializers.CharField(allow_blank=True, allow_null=True,required=False)
    password = serializers.CharField(
			style={'input_type': 'password'}, trim_whitespace=False
		)

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(
			style={'input_type': 'password'}, trim_whitespace=False
		)
