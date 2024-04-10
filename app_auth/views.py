from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema


from .serializers import *

User = get_user_model()

class RegistrationAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={status.HTTP_201_CREATED: 'User registration successful'},
    )
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response({
                "user" : UserRegistrationSerializer(user).data,
                "access" : token.access_token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)