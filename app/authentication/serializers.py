from rest_framework import serializers
from django.contrib.auth import get_user_model
from authentication.models import EmpactUser
from blog.serializers import Comment




User = get_user_model()

    
class EmpactUserSerializer(serializers.ModelSerializer):
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = EmpactUser
		fields = ['id', 'first_name','last_name','mobile_number', 'email', 'user_type','member_type','country', 'date_created','updated_on','comments' ]
		read_only_fields = ['id']
      
class EmpactUserWithoutCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmpactUser
		fields = ['id', 'first_name','last_name','mobile_number', 'email', 'user_type','member_type','country', 'date_created','updated_on',]
		read_only_fields = ['id']
      

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    mobile_no = serializers.CharField()
    email = serializers.EmailField()
    user_type = serializers.CharField()
    member_type = serializers.CharField()
    country = serializers.CharField()
    profile_pic_url = serializers.CharField(allow_blank=True, allow_null=True,required=False)
    password = serializers.CharField(
			style={'input_type': 'password'}, trim_whitespace=False
		)

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(
			style={'input_type': 'password'}, trim_whitespace=False
		)

class UserCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')


    class Meta:
        model = Comment
        fields = ['comment_id', 'body', 'owner', 'post']
