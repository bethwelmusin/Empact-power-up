from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    status = serializers.BooleanField()
    last_name = serializers.CharField()
    mobile_no = serializers.CharField()
    email = serializers.CharField()
    user_type = serializers.CharField()
    member_type = serializers.CharField()
    country = serializers.CharField()
    profile_pic_url = serializers.CharField(allow_blank=True, allow_null=True,required=False)
    password = serializers.CharField(
			style={'input_type': 'password'}, trim_whitespace=False
		)

