from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterSerializer(serializers.ModelSerializer):
 confirm_password=serializers.CharField(write_only=True)
 class Meta:
  model=User; fields=('first_name','last_name','email','password','confirm_password'); extra_kwargs={'password':{'write_only':True}}
 def validate_email(self,value):
  value=value.lower().strip()
  if User.objects.filter(email__iexact=value).exists(): raise serializers.ValidationError('An account with this email already exists.')
  return value
 def validate_password(self,value): validate_password(value); return value
 def validate(self,attrs):
  if attrs['password'] != attrs['confirm_password']: raise serializers.ValidationError({'confirm_password':['Passwords do not match.']})
  return attrs
 def create(self,validated_data):
  validated_data.pop('confirm_password'); email=validated_data.pop('email')
  return User.objects.create_user(username=email,email=email,password=validated_data.pop('password'),**validated_data)
class UserSerializer(serializers.ModelSerializer):
 class Meta: model=User; fields=('id','first_name','last_name','email')
class ChangePasswordSerializer(serializers.Serializer):
 old_password=serializers.CharField(write_only=True); new_password=serializers.CharField(write_only=True)
 def validate_new_password(self,value): validate_password(value); return value
