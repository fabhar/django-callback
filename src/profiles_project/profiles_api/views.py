from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})


class GetTokenViewSet(viewsets.ViewSet):
    """GetToken API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a user token."""

        data_set = [
            'By default, all Callbacks will return emails',
            'to admin: firdaus.abhar@gmail.com'
        ]

        return Response({'status': '0', 'data': data_set, 'accessToken': 'test', 'expiresTime': '0', 'message': 'none'})

    def create(self, request):
        """Create a new token for given userId."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('userId')
            message = 'Access token for: {0}'.format(name)
            return Response({'status': '0', 'data': '', 'accessToken': 'test', 'expiresTime': '0', 'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})

class SendAlarmViewSet(viewsets.ViewSet):
    """SendAlarm API ViewSet."""

    serializer_class = serializers.SendAlarmSerializer

    def list(self, request):
        return Response({'status': '0', 'message': 'none'})

    def create(self, request):
        """Create a new token for given userId."""

        serializer = serializers.SendAlarmSerializer(data=request.data)

        if serializer.is_valid():
            SMTPserver = 'smtp.gmail.com'
            sender = 'chelsea.rudde@gmail.com'
            destination = ['firdaus.abhar@gmail.com']
            USERNAME = "chelsea.rudde@gmail.com"
            PASSWORD = "PapaBosan1"

            # typical values for text_subtype are plain, html, xml
            text_subtype = 'plain'
            content="""\
            Test message
            """
            subject="Sent from Python"
            emailResult="sent"

            try:
                msg = MIMEText(content, text_subtype)
                msg['Subject']= subject
                msg['From'] = sender # some SMTP servers will do this automatically, not all

                conn = SMTP(SMTPserver)
                conn.set_debuglevel(False)
                conn.login(USERNAME, PASSWORD)
                try:
                    conn.sendmail(sender, destination, msg.as_string())
                finally:
                    conn.quit()

            except Exception, exc:
                emailResult = "mail failed"

            return Response({'status': '0', 'message': emailResult})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})



class SendFaultViewSet(viewsets.ViewSet):
    """SendFault API ViewSet."""

    serializer_class = serializers.SendFaultSerializer

    def list(self, request):
        return Response({'status': '0', 'message': 'none'})

    def create(self, request):
        """Create a new token for given userId."""

        serializer = serializers.SendFaultSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('userId')
            message = 'Access token for: {0}'.format(name)
            return Response({'status': '0', 'message': ""})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})




class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
