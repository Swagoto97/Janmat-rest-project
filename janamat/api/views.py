from rest_framework import generics
from django.contrib.auth.models import User, Group
from jmat.models import Timeline
from rest_framework import viewsets
from . serializers import UserSerializer, GroupSerializer, TimelineSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . pagination import LargeResultsSetPagination, StandardResultsSetPagination

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer






class Timeline_List(generics.ListCreateAPIView):
    queryset = Timeline.objects.all().order_by('-date_time')
    # queryset = Timeline.objects.all().order_by('-id')
    serializer_class = TimelineSerializer
    pagination_class = StandardResultsSetPagination


class Timeline_Update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all().order_by('-date_time')
    # queryset = Timeline.objects.all().order_by('-id')
    serializer_class = TimelineSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]







from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
class HelloView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


