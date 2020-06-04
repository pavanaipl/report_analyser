from rest_framework.permissions import BasePermission
from .encryption import crypto_decode, jwt_decode_handler
from .models import *


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        try:
            user_id = crypto_decode(
                jwt_decode_handler(
                    request.META['HTTP_AUTHORIZATION']
                )['ai']
            )
            pwd = crypto_decode(
                jwt_decode_handler(
                    request.META['HTTP_AUTHORIZATION']
                )['bi']
            )
            request.user = UsersDetails.objects.get(id=int(user_id), password=pwd, is_active=True)
            return True
        except:
            return False