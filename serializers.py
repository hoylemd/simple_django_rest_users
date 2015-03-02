from django.contrib.auth.models import User

from rest_framework import serializers
from charman.models import Character


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # example owned stuff link: snippets =
    #  serializers.HyperlinkedRelatedField(many=True,
    #                                      view_name='snippet-detail')
    characters = serializers.HyperlinkedRelatedField(many=True,
            view_name='character-detail',
            queryset=Character.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username')
