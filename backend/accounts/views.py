from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
