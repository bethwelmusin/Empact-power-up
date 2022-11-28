from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    status = serializers.BooleanField(default=False)
    status_code = serializers.CharField(default='400')
    message = serializers.CharField()
    errors = serializers.CharField()
    
