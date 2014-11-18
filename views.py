from django.contrib.auth.models import User

from simple_users.serializers import UserSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  """
  This viewset automatically provides 'list' and 'detail' actions
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
