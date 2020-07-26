from django.contrib.auth.models import User, Group
from jmat.models import Timeline
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class TimelineSerializer(serializers.HyperlinkedModelSerializer):
# class TimelineSerializer(ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['user', 'date_time', 'news_header', 'news']
        

