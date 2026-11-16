from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer
class RegisterView(generics.CreateAPIView):
 serializer_class=RegisterSerializer; permission_classes=[AllowAny]
 def create(self,request,*args,**kwargs):
  s=self.get_serializer(data=request.data); s.is_valid(raise_exception=True); user=s.save(); refresh=RefreshToken.for_user(user)
  return Response({'user':UserSerializer(user).data,'access':str(refresh.access_token),'refresh':str(refresh)},status=status.HTTP_201_CREATED)
class LoginView(APIView):
 permission_classes=[AllowAny]
 def post(self,request):
  email=request.data.get('email','').lower().strip(); password=request.data.get('password','')
  user=authenticate(request,username=email,password=password)
  if not user: return Response({'non_field_errors':['Invalid email or password.']},status=400)
  refresh=RefreshToken.for_user(user); return Response({'user':UserSerializer(user).data,'access':str(refresh.access_token),'refresh':str(refresh)})
class MeView(generics.RetrieveAPIView):
 serializer_class=UserSerializer; permission_classes=[IsAuthenticated]
 def get_object(self): return self.request.user
class ChangePasswordView(APIView):
 permission_classes=[IsAuthenticated]
 def put(self,request):
  s=ChangePasswordSerializer(data=request.data); s.is_valid(raise_exception=True)
  if not request.user.check_password(s.validated_data['old_password']): return Response({'old_password':['Old password is incorrect.']},status=400)
  request.user.set_password(s.validated_data['new_password']); request.user.save(); return Response({'detail':'Password changed successfully.'})
