from rest_framework import viewsets
from news.models import Users
from news_rest.serializers.user_serializer import UsersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
