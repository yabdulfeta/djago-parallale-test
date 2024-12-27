from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OperationSerializer

class AddView(APIView):
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operand1 = serializer.validated_data['operand1']
            operand2 = serializer.validated_data['operand2']
            result = operand1 + operand2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubtractView(APIView):
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operand1 = serializer.validated_data['operand1']
            operand2 = serializer.validated_data['operand2']
            result = operand1 - operand2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MultiplyView(APIView):
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operand1 = serializer.validated_data['operand1']
            operand2 = serializer.validated_data['operand2']
            result = operand1 * operand2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DivideView(APIView):
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operand1 = serializer.validated_data['operand1']
            operand2 = serializer.validated_data['operand2']
            if operand2 == 0:
                return Response({'error': 'Division by zero'}, status=status.HTTP_400_BAD_REQUEST)
            result = operand1 / operand2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)