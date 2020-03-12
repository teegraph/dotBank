from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    uuid = serializers.CharField(required=True)
    value = serializers.IntegerField(required=True)


class AccountStatusSerializer(serializers.Serializer):
    uuid = serializers.CharField(required=True)
