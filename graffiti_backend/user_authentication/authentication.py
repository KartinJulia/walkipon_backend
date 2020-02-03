from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

'''
https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
'''

class SessionAuthentication(authentication.BaseAuthentication):
    """
    Use Django's session framework for authentication.
    """

    def authenticate(self, request):
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """

        # Get the session-based user from the underlying HttpRequest object
        user = getattr(request._request, 'user', None)

        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active:
            return None

        #self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return (user, None)