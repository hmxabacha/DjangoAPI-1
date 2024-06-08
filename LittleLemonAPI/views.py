from django.shortcuts import render
from .serializers import CartSerializer,OrderSerializer,MenuItemSerializer,CategorySerailizer
from .models import Cart,MenuItem,Order,Category
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes,api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    model=MenuItem
    fields=['title','price','featured','category']
    @api_view()
    @permission_classes([IsAuthenticated])
    def ManagerView(request):
        if request.user.groups.filter(name='Manager').exists():
            return Response("Being a manager, you can see this!!")
        else:
            return Response({"You have no permission"},403)
    @api_view
    @permission_classes([IsAuthenticated])  
    def AdminView(request):
        if request.user.groups.filter(name='Admin').exist():
            return Response({"OK"})
        else:
            return Response({"you are not allowed!!"})
    
    @api_view
    @permission_classes
    def DeliveryCrewView(request):
        if request.user.groups.filter(name='DeliveryCrew').exist():
            return Response({"OK"})
        else:
            return Response({"not allowed!!"})
        
    @api_view
    @permission_classes
    def CustomerView(request):
        if request.user.groups.filter(name='Customer').exist():
            return Response({"OK"})
        else:
            return Response({"not allowed!!"})
        
        
    
        
        
        
    
