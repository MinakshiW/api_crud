from django.urls import path
from .api import *

urlpatterns = [
    path('emp/', EmployeeAPI),
    path('emp/<pk>/', EmployeeDetailsAPI),
]