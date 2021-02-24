from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password





class visitorSerializer(serializers.ModelSerializer):
        
	class Meta:
		model = Visitor
		fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
	username = serializers.CharField(write_only=True, required=True)
	# email = serializers.EmailField(
	# 		required=True,
	# 		validators=[UniqueValidator(queryset=User.objects.all())]
	# 		)

	password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

	def validate(self, attrs):
		if attrs['password1'] != attrs['password2']:
			raise serializers.ValidationError({"password": "Password fields didn't match."})

		return attrs

	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
#			email=validated_data['email'],
			password=validated_data['password1'],
			# first_name=validated_data['first_name'],
			# last_name=validated_data['last_name']
		)

		
		user.set_password(validated_data['password1'])
		user.save()

		return user