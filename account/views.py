from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser


from .models import User
from .serializers import (
    SignupSerializer,
    ProfileSerializer,
)

class SignupAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser,)
    lookup_field = 'username'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)