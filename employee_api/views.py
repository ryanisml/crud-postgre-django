from rest_framework import permissions, viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer