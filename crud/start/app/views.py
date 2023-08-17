from django.shortcuts import render, HttpResponse
from.models import Crop
from .serializers import CropSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def cropListView(request):
    if request.method == 'GET':
        detail = Crop.objects.all()
        serializer = CropSerializer(detail, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def cropDetailView(request, pk):
    try:
        employee = Crop.objects.get(pk=pk)
    except Crop.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CropSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        serializer = CropSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


