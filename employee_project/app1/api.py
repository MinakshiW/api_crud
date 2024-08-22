from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import EmployeeSerializer
from .models import Employee
from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(http_method_names=['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeAPI(request):

    if request.method == 'GET':
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeDetailsAPI(request, pk):

    if request.method == 'GET':
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data = request.data, instance= obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data = request.data, instance= obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        obj = get_object_or_404(Employee, pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


