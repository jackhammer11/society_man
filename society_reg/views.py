from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .forms import CreateSocietyForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .serializers import visitorSerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django import template
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user,allowed_user,admin_only
def home(request):

    return render(request,'society_reg/home.html')



def register(request):

	form =  CreateSocietyForm()
	if request.method == 'POST':
		form =  CreateSocietyForm(request.POST)
		#print(dir(form))
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
		
			messages.success(request,"Account was created for " + username)

			

			return redirect('home')
	context = {'register':form}
	return render(request,'society_reg/registration.html',context)


def visitor(request):
    visitors = Visitor.objects.all()

    context = {'visitors':visitors}

    return render(request,'society_reg/visitor.html',context)


@api_view(['GET', 'POST'])
def visitorList(request):


	if request.method == 'GET':
		visitors = Visitor.objects.all()
		serializer = visitorSerializer(visitors,many=True)

		return Response(serializer.data)

	elif request.method == 'POST':
		
		serializer = visitorSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def societyList(request):

	if request.method == 'GET':

		content = {
			'id': str(request.user.id),
			'user': str(request.user),
			'password': str(request.user.password),
			'auth': str(request.auth),  # None
		}
		return Response(content)



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer




@api_view(['GET', 'PUT', 'DELETE'])
def visitordetails(request,pk):
		try:
			visitors = Visitor.objects.get(id = pk)
		except Visitor.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer =  visitorSerializer(visitors)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer =  visitorSerializer(visitors, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			visitors.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)


@unauthenticated_user
def login_view(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')


		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request,'Username OR password is incorrect')



	context = {}
	return render(request,'society_reg/login.html',context)


def logout_view(request):
	logout(request)

	return redirect('login')

