from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  # example owned stuff link: snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

  class Meta:
    model = User
    fields = ('url', 'username')
