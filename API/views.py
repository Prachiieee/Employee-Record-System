from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import EmployeeDetailsSerialiser,DepartmentSerialiser,SkillSerialiser
from .models import EmployeeDetails,Department,Skills
from rest_framework.response import Response
from rest_framework import viewsets, status,permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Skills

# Create your views here.
def home(request):
    return HttpResponse('Welcome to our home page')

class EmpViewSet(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerialiser

    def list(self, request):
        # Handle GET /api/skill_api/
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Handle POST /api/skill_api/
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Handle GET /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Handle PUT /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Handle DELETE /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class DepartmentViewSet(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerialiser

    def list(self, request):
        # Handle GET /api/skill_api/
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Handle POST /api/skill_api/
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Handle GET /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Handle PUT /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Handle DELETE /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SkillViewSet(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Skills.objects.all()
    serializer_class = SkillSerialiser

    def list(self, request):
        # Handle GET /api/skill_api/
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Handle POST /api/skill_api/
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Handle GET /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Handle PUT /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Handle DELETE /api/skill_api/1/
        skill = get_object_or_404(self.queryset, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
