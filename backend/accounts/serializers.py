from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
