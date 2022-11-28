from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    status = serializers.BooleanField(default=False)
    status_code = serializers.CharField(default='400')
    messages = serializers.CharField()
    errors = serializers.CharField()
    