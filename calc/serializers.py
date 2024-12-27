from rest_framework import serializers

class OperationSerializer(serializers.Serializer):
    operand1 = serializers.FloatField()
    operand2 = serializers.FloatField()